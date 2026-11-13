#include "fifo_evictor.hh"

FifoEvictor::~FifoEvictor() {}

void FifoEvictor::touch_key(const key_type &key) { queue.push(key); }

const key_type FifoEvictor::evict()
{
  if (queue.size() == 0) {
    return "";
  }
  auto ret = queue.front();
  queue.pop();
  return ret;
}
