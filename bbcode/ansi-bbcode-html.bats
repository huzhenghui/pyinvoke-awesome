#!/usr/bin/env bats

@test "convert 1m to b to strong" {
    result="$(echo -e "convert 1m \033[1mto b to\033[0m strong" | ansifilter --bbcode | inv bbcode-parser-format)"
    [ "$result" == "convert 1m <strong>to b to</strong> strong<br />" ]
}

@test "convert 3m to i to em" {
    result="$(echo -e "convert 3m \033[3mto i to\033[0m em" | ansifilter --bbcode | inv bbcode-parser-format)"
    [ "$result" == "convert 3m <em>to i to</em> em<br />" ]
}

@test "convert 4m to u to strong" {
    result="$(echo -e "convert 4m \033[4mto u to\033[0m strong" | ansifilter --bbcode | inv bbcode-parser-format)"
    [ "$result" == "convert 4m <strong>to u to</strong> strong<br />" ]
}