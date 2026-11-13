#pragma once

#include "evictor.hh"
#include <queue>

class FifoEvictor : public Evictor {
    public:
  FifoEvictor() = default;
  ~FifoEvictor() override;
  void touch_key(const key_type &key) override;
  const key_type evict() override;

    protected:
  std::queue<key_type> queue;
};
