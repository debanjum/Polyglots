TARGET = baudotmessage
CFLAGS = -Wall -pedantic -std=c99

# compile
all: $(TARGET) etags
$(TARGET):
	$(CC) $(CFLAGS) $(TARGET).c -o $(TARGET)
etags:
	find . -name '*.[ch]' | xargs etags

# run message_generation, main grc script
polyglot:
	python polyglot.py
message:
	./$(TARGET)
	python varicodemessage.py
run: message polyglot

# clean up
.PHONY: clean
clean:
	rm -f $(TARGET)
	rm -f *.pyc
	rm -f *.bin
	rm -f TAGS
