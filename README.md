# Lesson-07-TestDrivenDev
### 1. Test-driven Development
Test-driven development (TDD) is a software development process that relies on the repetition of a very short development cycle: requirements are turned into very specific test cases, then the code is improved so that the tests pass. This is opposed to software development that allows code to be added that is not proven to meet requirements.

### 2. Test-driven development cycle
1. Add a test
In test-driven development, each new feature begins with writing a test. Write a test that defines a function or improvements of a function, which should be very succinct. To write a test, the developer must clearly understand the feature's specification and requirements. The developer can accomplish this through use cases and user stories to cover the requirements and exception conditions, and can write the test in whatever testing framework is appropriate to the software environment. It could be a modified version of an existing test. This is a differentiating feature of test-driven development versus writing unit tests after the code is written: it makes the developer focus on the requirements before writing the code, a subtle but important difference.
2. Run all tests and see if the new test fails
This validates that the test harness is working correctly, shows that the new test does not pass without requiring new code because the required behavior already exists, and it rules out the possibility that the new test is flawed and will always pass. The new test should fail for the expected reason. This step increases the developer's confidence in the new test.
3. Write the code
The next step is to write some code that causes the test to pass. The new code written at this stage is not perfect and may, for example, pass the test in an inelegant way. That is acceptable because it will be improved and honed in Step 5.
At this point, the only purpose of the written code is to pass the test. The programmer must not write code that is beyond the functionality that the test checks.
4. Run tests
If all test cases now pass, the programmer can be confident that the new code meets the test requirements, and does not break or degrade any existing features. If they do not, the new code must be adjusted until they do.
5. Refactor code
The growing code base must be cleaned up regularly during test-driven development. New code can be moved from where it was convenient for passing a test to where it more logically belongs. Duplication must be removed. Object, class, module, variable and method names should clearly represent their current purpose and use, as extra functionality is added. As features are added, method bodies can get longer and other objects larger. They benefit from being split and their parts carefully named to improve readability and maintainability, which will be increasingly valuable later in the software lifecycle. Inheritance hierarchies may be rearranged to be more logical and helpful, and perhaps to benefit from recognized design patterns. There are specific and general guidelines for refactoring and for creating clean code.[6][7] By continually re-running the test cases throughout each refactoring phase, the developer can be confident that process is not altering any existing functionality.
The concept of removing duplication is an important aspect of any software design. In this case, however, it also applies to the removal of any duplication between the test code and the production code—for example magic numbers or strings repeated in both to make the test pass in Step 3.

### 3. Basic Example
Requirement:  
Complete a method receiving a string and return the reverse word.  

In test-driven development, we are going to write a test to test the feature.
```
class TestReverse(unittest.TestCase):
    def test_get_reverse(self):
        self.assertEqual(reverseword.get_reverse('apple'), 'elppa')
        self.assertEqual(reverseword.get_reverse('orange'), 'egnaro')
```

After validating all tests successfully, complete the feature.
```
def get_reverse(str):
    return str[::-1]
```

### 4. Exercise
Requirement:   
Complete a method receiving a string and return the array of all anagrams.  
Complete a method receiving a string and return the number of anagrams.  
Complete 'test_anagrams.py' and 'anagrams.py' based on test-driven development. 
 
1.Complete 'test_anagrams.py' to test two methods, one of which checks the array of anagrams and another one checks the number of anagrams.  
2.Complete 'anagrams.py' according to test file.