#include "cache.hh"
#include <cstring>
#include <memory>
#include <unordered_map>

class Cache::Impl {
    public:
  // Hash map value
  class MapNode {
      public:
    MapNode(Cache::size_type s, Cache::val_type v) : size_(s), val_(v) {}
    MapNode(const Cache &) = delete;
    MapNode &operator=(const Cache &) = delete;
    Cache::size_type size() const { return size_; }
    Cache::val_type val() const { return val_; }

    ~MapNode() { free((void *)val_); }

      private:
    Cache::size_type size_;
    Cache::val_type val_;
  };

  Impl(Cache::size_type maxmem, float max_load_factor, Evictor *evictor,
       Cache::hash_func hasher)
      : maxmem(maxmem), evictor(evictor), hasher(hasher), current_mem(0)
  {
    auto comp = [](key_type k1, key_type k2) { return k1 == k2; };
    map =
        std::unordered_map<key_type, std::unique_ptr<MapNode>, Cache::hash_func,
                           std::function<bool(key_type, key_type)>>(0, hasher,
                                                                    comp);
    map.max_load_factor(max_load_factor);
  }

  ~Impl()
  {
    // A Cache does not own the Evictor,
    // while the values are owned from MapNode
  }

  // owned values
  Cache::size_type maxmem;
  Evictor *evictor;
  Cache::hash_func hasher;
  std::unordered_map<key_type, std::unique_ptr<MapNode>, Cache::hash_func,
                     std::function<bool(key_type, key_type)>>
      map;
  Cache::size_type current_mem;

  // owned functions
  void resize();
};

Cache::Cache(Cache::size_type maxmem, float max_load_factor, Evictor *evictor,
             Cache::hash_func hasher)
    : pImpl_(new Cache::Impl(maxmem, max_load_factor, evictor, hasher))
{
}

Cache::~Cache()
{
  // cache holds only a unique ptr to Impl, which will be
  // cleaned up on drop
  // it also must clean up the map
}

// Cache::set: Adds a value to the cache
//
// key_type key: the key
// Cache::val_type val: the value
// Cache::size_type size: the size of the value in size_type
void Cache::set(key_type key, Cache::val_type val, Cache::size_type size)
{
  Cache::size_type current = 0;
  // get necessary to retrieve size of possible old entry
  // with the same key
  get(key, current);

  auto newsize = size + pImpl_->current_mem - current;
  if (newsize > pImpl_->maxmem) {
    if (pImpl_->evictor == nullptr || size > pImpl_->maxmem) {
      // no evictor => no evictions
      // to big to store => why bother evicting
      return;
    }
    while (pImpl_->current_mem + size > pImpl_->maxmem) {
      key_type k = pImpl_->evictor->evict();
      del(k);
    }
  }
  del(key);
  pImpl_->current_mem += size;

  // cleaned up in Cache::del
  // all values deleted on drop
  void *copy_val = malloc(size);
  // val better be a pointer
  memcpy(copy_val, val, size);
  pImpl_->map[key] = std::unique_ptr<Cache::Impl::MapNode>(
      new Cache::Impl::MapNode(size, (Cache::val_type)copy_val));
  if (pImpl_->evictor != nullptr) {
    pImpl_->evictor->touch_key(key);
  }
}

// Cache::get: retrieve a value from the cache
//
// key_type key: a key
// Cache::size_type &val_size: where to place the size of the associated value
//
// return Cache::val_type: the value associated with key

Cache::val_type Cache::get(key_type key, Cache::size_type &val_size) const
{
  auto search = pImpl_->map.find(key);
  if (search != pImpl_->map.end()) {
    if (pImpl_->evictor != nullptr) {
      pImpl_->evictor->touch_key(search->first);
    }
    val_size = search->second->size();
    return search->second->val();
  }
  else {
    val_size = 0;
    return nullptr;
  }
}

// Cache::del: Delete a value from the cache
//
// key_type key: a key
//
// return bool: if the value was found
bool Cache::del(key_type key)
{
  auto found = pImpl_->map.find(key);
  if (found != pImpl_->map.end()) {
    pImpl_->current_mem -= found->second->size();
    // we have found a value to delete
    pImpl_->map.erase(key);
    return true;
  }
  else {
    return false;
  }
}

// Cache::space_used: The amount of memory used by the cache

Cache::size_type Cache::space_used() const { return pImpl_->current_mem; }

// Cache::reset: Removes all elements from the cache

void Cache::reset()
{
  pImpl_->current_mem = 0;
  pImpl_->map.clear();
}
