import scala.io.Source
import scala.util.matching.Regex
import scala.util.matching.Regex._
import scala.util.chaining._
import scala.math._

@main def main(day: Int): Unit =
    day match
        case 1 => 
            println("Day 1:")
            println("Part 1:\n"+
                Source.fromFile("./Puzzle Inputs/day1.txt").getLines.map(line =>
                    10*line.filter(_.isDigit)(0).asDigit + line.filter(_.isDigit).reverse(0).asDigit
                ).sum
            )
            println("Part 2:\n"+
                Source.fromFile("./Puzzle Inputs/day1.txt").getLines.map(line =>
                    ((patterns: Array[String]) =>
                        Array(
                            patterns.mkString("(","|",")").r.unanchored.findAllMatchIn(line).next.group(1),
                            patterns
                                .map(x => if !x.contains('[') then x.reverse else x)
                                .reverse.mkString("(","|",")").r.unanchored
                            .findAllMatchIn(line.reverse).next.group(1)
                        )
                    ).apply(Array("[0-9]", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")).map(y =>
                        if y(0).isDigit then
                            y.toInt
                        else
                            Array(y, y.reverse).map(
                                Map("one"->1,"two"->2,"three"->3,"four"->4,"five"->5,"six"->6,"seven"->7,"eight"->8,"nine"->9)
                                    .getOrElse(_,0)
                            ).sum
                    ).reduceLeft(10*_ + _)
                ).sum
            )
        case 2 =>
            println("Day 2:")
            println("Part 1:\n"+
                Source.fromFile("./Puzzle Inputs/day2.txt").getLines.map(
                    "Game ([0-9]+): (.*)".r.findFirstMatchIn(_).map(matches =>
                        matches.group(2).split("; ").map(
                            "([0-9]+) (red|blue|green)".r.findAllMatchIn(_).foldRight(true)((item, accum) =>
                                (Map("red" -> 12, "green" -> 13, "blue" -> 14)(item.group(2)) >= item.group(1).toInt) && accum
                            )
                        ).foldRight(matches.group(1).toInt)((a, b) => if a then b else 0)
                    ).getOrElse(0)
                ).sum
            )
            println("Part 2:\n"+
                Source.fromFile("./Puzzle Inputs/day2.txt").getLines.map(line =>
                    "Game ([0-9]+): (.*)".r.findFirstMatchIn(line).map(matches =>
                        Array(
                            "([0-9]+) red".r.findAllMatchIn(matches.group(2)).map(_.group(1).toInt).max,
                            "([0-9]+) green".r.findAllMatchIn(matches.group(2)).map(_.group(1).toInt).max,
                            "([0-9]+) blue".r.findAllMatchIn(matches.group(2)).map(_.group(1).toInt).max
                        ).product
                    ).getOrElse(0)
                ).sum
            )
        case 3 =>
            println("Day 3:")
            println("Part 1:\n"
                /*Source.fromFile("./Puzzle Inputs/day3.txt").getLines
                    .toArray
                    .zipWithIndex
                    .pipe(linesArray =>
                        linesArray.map((line, lindex) =>
                            line.zipWithIndex
                                .filter(a => "!@#$%^&*-+=/".toArray.contains(a._1))
                                .map((char, chardex) =>
                                    Array(-1, 0, 1)
                                        .flatMap(x => Array(-1, 0, 1).map(y => (x, y)))
                                        .map(offset =>
                                            linesArray(lindex+offset._1)(chardex+offset._2).pipe(charInQuestion =>
                                                if charInQuestion.isDigit then
                                                    1
                                                else 0
                                            )
                                        )
                                )
                        )
                    )*/
            )
        case 4 =>
            println("Day 4:")
            println("Part 1:\n"+
                Source.fromFile("./Puzzle Inputs/day4.txt").getLines.map(_.split(':').pipe(splitColon =>
                        splitColon(1).split('|').map(splitBar =>
                            Set(splitBar.split(' ').filter(_.nonEmpty).map(_.toInt)*)
                        ).reduceLeft((a, b) => a.intersect(b)).size.pipe(x => pow(2,x-1).toInt)
                    )
                ).sum
            )
            println("Part 2:\n")

        case _ => println("Invalid day")