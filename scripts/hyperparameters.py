from os.path import join

#: Not actually used directly, just for convenience
DATA_DIR = "/home/fringant2/lisa/turian/dev/python/language-model.predict-final-word/data/"

#TRAIN_SENTENCES = join(DATA_DIR, "allwords.train.gz")
##VALIDATION_SENTENCES = join(DATA_DIR, "allwords.validation.gz")
#VALIDATION_SENTENCES = join(DATA_DIR, "allwords.validation-100.gz")
#VOCABULARY = join(DATA_DIR, "allwords.vocabulary-5000.txt")

TRAIN_SENTENCES = join(DATA_DIR, "wikitext.train.txt.gz")
#VALIDATION_SENTENCES = join(DATA_DIR, "wikitext.validation.txt")
VALIDATION_SENTENCES = join(DATA_DIR, "wikitext.validation-200.txt")
#VALIDATION_SENTENCES = join(DATA_DIR, "wikitext.validation-100.txt")
#VOCABULARY = join(DATA_DIR, "vocabulary-wikitext-10000.txt.gz")
VOCABULARY = {5000: join(DATA_DIR, "vocabulary-wikitext-5000.txt.gz"),
10000: join(DATA_DIR, "vocabulary-wikitext-10000.txt.gz"),
20000: join(DATA_DIR, "vocabulary-wikitext-20000.txt.gz")}

#VOCABULARY_SIZE = 5000
#VOCABULARY_SIZE = 10000
VOCABULARY_SIZE = 20000

# Each embedded word representation has this width
EMBEDDING_SIZE = 50
#EMBEDDING_SIZE = 5

# Predict with a window of five words at a time
WINDOW_SIZE = 5

HIDDEN_SIZE = 100
#HIDDEN_SIZE = 10

#: Scaling value to control range for weight initialization
#SCALE_INITIAL_WEIGHTS_BY = math.sqrt(3)
SCALE_INITIAL_WEIGHTS_BY = 1

# Which activation function to use?
#ACTIVATION_FUNCTION="sigmoid"
#ACTIVATION_FUNCTION="tanh"
ACTIVATION_FUNCTION="softsign"

LEARNING_RATE = 0.001
#LEARNING_RATE = 0.01
#LEARNING_RATE = 0.1

## number of (higher-order) quadratic filters for James's neuron
#NUMBER_OF_QUADRATIC_FILTERS=0
## We use this scaling factor for initial weights of quadratic filters,
## instead of SCALE_INITIAL_WEIGHTS_BY
## @note: Try between 10 and 0.01
#SCALE_QUADRATIC_INITIAL_WEIGHTS_BY = 1

# Validate after this many examples
VALIDATE_EVERY = 1000000
#VALIDATE_EVERY = 1000
