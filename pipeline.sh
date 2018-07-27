#!/bin/bash


ml-run-process example.HelloPersonWithOutput -o output:file1.txt -p person:Jerry
ml-run-process example.Replace -i input:file1.txt -o output:file2.txt -p search:Jerry replace:Jeremy
ml-run-process example.Colorize -i input:file2.txt -o output:file3.txt -p color:yellow
