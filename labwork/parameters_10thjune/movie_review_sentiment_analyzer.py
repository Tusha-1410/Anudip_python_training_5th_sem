# Movie Review Sentiment Analyzer

# List of movie reviews
reviews = [
    "excellent movie",
    "average story",
    "excellent acting",
    "poor direction",
    "excellent visuals",
    "poor screenplay",
    "good music",
    "excellent climax",
    "average performance",
    "good cinematography"
]

# --------------------------------------------------
# Function 1: Count review sentiments

def count_sentiments(reviews):

    excellent = 0
    good = 0
    average = 0
    poor = 0

    # Check each review
    for review in reviews:

        if "excellent" in review:
            excellent += 1

        elif "good" in review:
            good += 1

        elif "average" in review:
            average += 1

        elif "poor" in review:
            poor += 1

    return excellent, good, average, poor


# --------------------------------------------------
# Function 2: Find the most common word

def most_common_word(reviews):

    word_count = {}

    # Visit each review
    for review in reviews:

        # Split review into words
        words = review.split()

        for word in words:

            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    # Find word with highest frequency
    most_common = ""
    highest_count = 0

    for word in word_count:

        if word_count[word] > highest_count:
            highest_count = word_count[word]
            most_common = word

    return most_common


# --------------------------------------------------
# Function 3: Find the longest review

def longest_review(reviews):

    longest = reviews[0]

    for review in reviews:

        if len(review) > len(longest):
            longest = review

    return longest


# --------------------------------------------------
# Function 4: Display reviews containing a keyword

def reviews_with_keyword(reviews, keyword):

    print("\nReviews containing '" + keyword + "':")

    for review in reviews:

        if keyword in review:
            print(review)


# --------------------------------------------------
# Main Program

excellent, good, average, poor = count_sentiments(reviews)

print("Excellent Reviews:", excellent)
print("Good Reviews:", good)
print("Average Reviews:", average)
print("Poor Reviews:", poor)

print("\nMost Common Word:",
      most_common_word(reviews))

print("\nLongest Review:",
      longest_review(reviews))

reviews_with_keyword(reviews, "excellent")
