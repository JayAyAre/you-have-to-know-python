"""
    Why you can’t avoid testing your code

        An important duty for developers is to test the newly created code, but you must not forget that testing
            isn't a way to prove that the code is error-free. Paradoxically, the only proof testing can provide is
            that your code contains errors. Don’t think you can relax after a successful test.

        The second important aspect of software testing is strictly psychological. It's a truth known for years that authors –
            even those who are reliable and self-aware – aren't able to objectively evaluate and verify their works.

        This is why each novelist needs an editor and each programmer needs a tester. Some say – a little spitefully but truthfully
            – that developers test the code to show their perfection, not to find problems that may frustrate them. Testers are
            free of such dilemmas, and this is why their work is more effective and profitable.

        Of course, this doesn't absolve you from being attentive and careful. Test your code as best you can.
            Don't make the testers' work too easy.

        Your primary duty is to ensure that you’ve checked all execution paths your code can go through.
            Does that sound mysterious? Nothing of the kind!
"""

temperature = float(input('Enter current temperature:'))

if temperature > 0:
    print("Above zero")
elif temperature < 0:
    print("Below zero")
else:
    print("Zero")

# Here we've tested the code for three different cases. but still, we haven't covered all the possible cases.

try:
    temperature = float(input('Enter current temperature:'))
    if temperature > 0:
        print("Above zero")
    elif temperature < 0:
        print("Below zero")
    else:
        print("Zero")
except ValueError:
    print('I do not know what to do.')

# Lets try this:

temperature = float(input('Enter current temperature:'))

if temperature > 0:
    print("Above zero")
elif temperature < 0:
    prin("Below zero")  # Python will raise an exception here
else:
    print("Zero")

"""
    Tests, testing, and testers

        The answer is simpler than you may expect, and a bit disappointing, too. Python – as you know for sure – is an
            interpreted language. This means that the source code is parsed and executed at the same time. Consequently,
            Python may not have time to analyze the code lines which aren't subject to execution. As an old developer's
            saying states: "it's a feature, not a bug" (please don't use this phrase to justify your code's weird behavior).

    Bug vs. debug

        The basic measure a developer can use against bugs is – unsurprisingly – a debugger, while the process during which
            bugs are removed from the code is called debugging.

        A debugger is a specialized piece of software that can control how your program is executed. Using the debugger,
            you can execute your code line-by-line, inspect all the variables' states and change their values on demand
            without modifying the source code,
            stop program execution when certain conditions are or aren't met, and do lots of other useful tasks.

    print debugging

        This form of debugging, which can be applied to your code using any kind of debugger, is sometimes called interactive debugging.
            The meaning of the term is self-explanatory – the process needs your (the developer's) interaction to be performed.

        You may use one of the simplest and the oldest (but still useful) debugging tactics known as print debugging.
            The name speaks for itself – you just insert several additional print() invocations inside your code to output
            data which illustrates the path your code is currently negotiating. You can output the values of the variables
            which may affect the execution.

        These printouts may output meaningful text like "I am here", "I entered the foo() function",
            "The result is 0", or they may contain sequences of characters that are legible only to you.
            Please don't use obscene or indecent words for the purpose,
            even though you may feel a strong temptation – your reputation can be ruined in a moment if these antics leak to the public.

    Some useful tips

        1. Try to tell someone (for example, your friend or coworker) what your code is expected to do and how it actually behaves.
            Be concrete and don't omit details.  Answer all questions your helper asks. You'll likely realize the cause of the problem
            while telling your story, as speaking activates these parts of your brain which remain idle during coding.
            If no human can help you with the problem, use a yellow rubber duck instead.
            We're not kidding – consult the Wikipedia article to learn more about this commonly used technique: Rubber Duck Debugging.
            https://en.wikipedia.org/wiki/Rubber_duck_debugging

        2. Try to isolate the problem. You can extract the part of your code that is suspected of being responsible for your troubles
            and run it separately.
            ou can comment out parts of the code that obscure the problem. Assign concrete values to variables instead of reading them from the input.

        3. If the bug has appeared recently and didn't show up earlier, analyze all the changes you've introduced into your code

        4. Take a break, drink a cup of coffee, take your dog and go for a walk, read a good book for a moment or two.

        5. Be optimistic – you'll find the bug eventually; we promise you this.

    Unit testing – a higher level of coding

        There is also one important and widely used programming technique that you will have to adopt sooner or later
            during your developer career – it's called unit testing. The name may a bit confusing,
            as it's not only about testing the software, but also (and most of all) about how the code is written.

        To standardize this approach and make it easier to apply, Python provides a dedicated module named unittest.
            We're not going to discuss it here – it's a broad and complex topic.

        Therefore, we’ve prepared a separate course and certification path for this subject.
            It is called “Testing Essentials with Python”, and we invite you to participate in it.
"""
