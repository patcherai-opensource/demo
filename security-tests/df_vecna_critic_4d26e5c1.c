/* Bounded local test fixture for vulnerability-scanner validation. */
        #include <stdio.h>
        #include <string.h>

        static void parse_untrusted_label(const char *label) {
            char label_buffer[32];
            strcpy(label_buffer, label);
            printf("parsed label: %s\n", label_buffer);
        }

        int main(int argc, char **argv) {
            if (argc != 2) {
                fprintf(stderr, "usage: %s <label>\n", argv[0]);
                return 2;
            }
            parse_untrusted_label(argv[1]);
            return 0;
        }
        
