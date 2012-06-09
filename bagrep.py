#!/usr/bin/env python
import sys

#------------------------------------------------------------------------------
def bagrep(data_input,pattern,before=2, after=2):
    """ Handles the grepping and before and after buffers
    """
    before_buffer = []
    after_buffer = None
    line = data_input.readline()

    matched_line = False

    while line:
        line = line.strip()

        if line and pattern in line:
            matched_line = True

        if matched_line:
            matched_line = False
            if before_buffer:
                print "\n".join( before_buffer )
            print "M:%s" % line
            after_buffer = []
            line = data_input.readline()
            continue

        if type(after_buffer).__name__ == "list":
            after_buffer.append("A:%s" % line)

        if after_buffer and len( after_buffer ) > after:
            print "\n".join( after_buffer )
            print "..."
            after_buffer = None
            

        before_buffer.append("B:%s" % line)
        if len( before_buffer ) > before:
            before_buffer.pop(before)

        line = data_input.readline()


#------------------------------------------------------------------------------
def main():
    """ main method: used for reading options and calling bagrep
    """

    file_name = None
    pattern = None

    if len(sys.argv) == 1:
        print """usage: %s [ pattern [ file ]]
Match a pattern in a file (or stdin) and print n lines of context before
and after the line"""
        sys.exit(1)

    if len(sys.argv) == 3:
        file_name = sys.argv[2]
        pattern = sys.argv[1]
    if len(sys.argv) == 2:
        pattern = sys.argv[1]

    if file_name:
            data_input = open(file_name, "rt")
    else:
        file_name = "stdin"
        data_input = sys.stdin

    bagrep(data_input,pattern)


#------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
