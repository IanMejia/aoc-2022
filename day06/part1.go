package part1

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {

	if lines, err := readLines("input.txt"); err == nil {
		for _, line := range lines {
            fmt.Println(line)
		}
	} else {
		log.Fatalf("readLines: %s", err)
	}
}

func readLines(path string) ([]int, error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var lines []int
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		if mass, err := strconv.Atoi(scanner.Text()); err == nil {
			lines = append(lines, mass)
		}
	}

	return lines, scanner.Err()
}
