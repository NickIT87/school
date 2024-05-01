/*
g++ -std=c++14 -I/opt/homebrew/Cellar/googletest/1.14.0/include -L/opt/homebrew/Cellar/googletest/1.14.0/lib -lgtest -lgtest_main -pthread example.cpp -o example_test
*/
#include <gtest/gtest.h>

// Example function to test
int add(int a, int b) {
    return a + b;
}

// A test case
TEST(AddTest, PositiveNumbers) {
    EXPECT_EQ(add(2, 3), 5);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
