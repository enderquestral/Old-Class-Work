#include "fifo_evictor.hh"
#include "lru_evictor.hh"
#include <cassert>
#include <catch2/catch.hpp>
#include <cstring>
#include <iostream>
#include <vector>
using namespace std;

TEST_CASE("fifo", "[evictor]")
{
  FifoEvictor e;
  SECTION("basic")
  {
    vector<char const *> s = {"foo", "bar", "baz", "bim", "bam", "bol"};
    REQUIRE(e.evict() == "");
    for (unsigned long i = 0; i < s.size(); i++) {
      e.touch_key(s[i]);
    }
    for (unsigned long i = 0; i < s.size(); i++) {
      REQUIRE(e.evict() == s[i]);
    }
    REQUIRE(e.evict() == "");
  }

  SECTION("duplicates")
  {
    vector<char const *> s = {"foo", "bar", "baz", "bim", "bam", "bol"};
    REQUIRE(e.evict() == "");
    for (unsigned long i = 0; i < s.size(); i++) {
      e.touch_key(s[i]);
    }
    for (unsigned long i = 0; i < s.size(); i++) {
      e.touch_key(s[i]);
    }
    for (unsigned long i = 0; i < s.size(); i++) {
      REQUIRE(e.evict() == s[i]);
    }
    for (unsigned long i = 0; i < s.size(); i++) {
      REQUIRE(e.evict() == s[i]);
    }
    REQUIRE(e.evict() == "");
  }

  SECTION("unsafe item")
  {

    REQUIRE(e.evict() == "");
    for (unsigned long i = 0; i < 20; i++) {
      e.touch_key(to_string(i).c_str());
    }
    for (unsigned long i = 0; i < 20; i++) {
      REQUIRE(e.evict() == to_string(i).c_str());
    }
    REQUIRE(e.evict() == "");
  }
}

TEST_CASE("lru", "[evictor]")
{
  LruEvictor e;
  vector<char const *> s = {"foo", "bar", "baz", "bim", "bam", "bol"};
  SECTION("basic")
  {
    REQUIRE(e.evict() == "");
    for (unsigned long i = 0; i < s.size(); i++) {
      e.touch_key(s[i]);
    }
    for (unsigned long i = 0; i < s.size(); i++) {
      REQUIRE(e.evict() == s[i]);
    }
    REQUIRE(e.evict() == "");
  }

  SECTION("juggle")
  {
    for (unsigned long i = 0; i < s.size(); i++) {
      e.touch_key(s[i]);
      e.touch_key(s[0]);
    }
    for (unsigned long i = 1; i < s.size(); i++) {
      REQUIRE(e.evict() == s[i]);
    }
    REQUIRE(e.evict() == s[0]);
    REQUIRE(e.evict() == "");
  }

  SECTION("unsafe item")
  {

    REQUIRE(e.evict() == "");
    for (unsigned long i = 0; i < 20; i++) {
      e.touch_key(to_string(i).c_str());
    }
    for (unsigned long i = 0; i < 20; i++) {
      REQUIRE(e.evict() == to_string(i).c_str());
    }
    REQUIRE(e.evict() == "");
  }
}
