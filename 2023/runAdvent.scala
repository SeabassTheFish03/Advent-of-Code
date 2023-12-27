import scala.io.Source
import scala.util.matching.Regex
import scala.util.matching.Regex._
import scala.util.chaining._
import scala.math._
import scala.collection.mutable.Stack

def day1part1(file: Iterator[String]): Int =
    file.map(line => 10*line.filter(_.isDigit)(0).asDigit + line.filter(_.isDigit).reverse(0).asDigit).sum
def day1part2(file: Iterator[String]): Int =
    file.map(line =>
        Array("[0-9]","one","two","three","four","five","six","seven","eight","nine").pipe(patterns =>
            Array(
                patterns.mkString("(","|",")").r.unanchored.findAllMatchIn(line).next.group(1),
                patterns.map(x => if x.contains('[') then x else x.reverse)
                    .reverse.mkString("(","|",")").r.unanchored
                    .findAllMatchIn(line.reverse).next.group(1)
            )
        ).map(y =>
            y.toIntOption.getOrElse(
                Array(y, y.reverse).map(
                    Map("one"->1,"two"->2,"three"->3,"four"->4,"five"->5,"six"->6,"seven"->7,"eight"->8,"nine"->9)
                        .getOrElse(_,0)
                ).sum
            )
        ).reduceLeft(10*_ + _)
    ).sum
            
def day2part1(file: Iterator[String]): Int =
    file.map(
        "Game ([0-9]+): (.*)".r.findFirstMatchIn(_).map(matches =>
            matches.group(2).split("; ").map(
                "([0-9]+) (red|blue|green)".r.findAllMatchIn(_).foldRight(true)((item, accum) =>
                    (Map("red" -> 12, "green" -> 13, "blue" -> 14)(item.group(2)) >= item.group(1).toInt) && accum
                )
            ).foldRight(matches.group(1).toInt)((a, b) => if a then b else 0)
        ).getOrElse(0)
    ).sum
def day2part2(file: Iterator[String]): Int =
    file.map(line =>
        "Game ([0-9]+): (.*)".r.findFirstMatchIn(line).map(matches =>
            Array(
                "([0-9]+) red".r.findAllMatchIn(matches.group(2)).map(_.group(1).toInt).max,
                "([0-9]+) green".r.findAllMatchIn(matches.group(2)).map(_.group(1).toInt).max,
                "([0-9]+) blue".r.findAllMatchIn(matches.group(2)).map(_.group(1).toInt).max
            ).product
        ).getOrElse(0)
    ).sum

def day3part1(file: Iterator[String]): Int =
    def absorbLeft(startIndex: Int, rawknit: String): String =
        if rawknit.lift(startIndex + 1).getOrElse(' ').isDigit then
            (rawknit(startIndex).toString.concat(absorbLeft(startIndex + 1, rawknit)))
        else rawknit(startIndex).toString

    file.toArray.mkString(".").pipe(rawknit => rawknit.toArray.zipWithIndex
        .filter((c, dex) => c.isDigit && !rawknit.lift(dex - 1).getOrElse(' ').isDigit)
        .map((c, dex) => (absorbLeft(dex, rawknit).toInt, dex))
        .filter((num, dex) =>
            (0 to log10(num).toInt).map(offset =>
                ((index: Int) =>
                    Set(-1, 0, 1).flatMap(offsety =>
                        Set(-1, 0, 1).map(offsetx =>
                            (Source.fromFile("./Puzzle Inputs/day3.txt").getLines.next.length + 1)
                                .pipe(lineLength => rawknit.lift(index + lineLength*offsety + offsetx).getOrElse(' '))
                        )
                    )
                ).apply(dex + offset).intersect("=&#+$/*%-@".toSet).nonEmpty
            ).reduce(_ || _)
        ).map(_._1).sum
    )
def day3part2(file: Iterator[String]): Int = ???

def day4part1(file: Iterator[String]): Int =
    file.map(_.split(':')(1).split('|')
        .map(splitBar =>
            Set(splitBar.split(' ').filter(_.nonEmpty).map(_.toInt)*)
        ).reduceLeft((a, b) => a.intersect(b)).size.pipe(x => pow(2,x-1).toInt)
    ).sum
def day4part2(file: Iterator[String]): Int =
    var lines = Stack(file
        .map(_.split(':')(1).split('|')
            .map(splitBar =>
                Set(splitBar.split(' ').filter(_.nonEmpty).map(_.toInt)*)
            )
        ).toArray*
    )
    var winCounter = new Array(lines.size)

    def wins(line: Array[Set[Int]]): Int = line.reduce(_.intersect(_)).size

    while lines.nonEmpty do
        ???
    3

def day5part1(file: Iterator[String]): Int = ???
def day5part2(file: Iterator[String]): Int = ???

def day9part1(file: Iterator[String]): Int =
    def slidingWindow(seq: Array[Int]): (Array[Int], Int) =
        if seq.sum == 0 then (seq, 0)
        else slidingWindow(seq.sliding(2).map(x => x(1)-x(0)).toArray).pipe((_, ph) =>
            (seq, seq.last + ph)
        )

    file.map(_.split(" ").map(_.toInt).pipe(slidingWindow(_))._2).sum
def day9part2(file: Iterator[String]): Int =
    def slidingWindow(seq: Array[Int]): (Array[Int], Int) =
        if seq.sum == 0 then (seq, 0)
        else slidingWindow(seq.reverse.sliding(2).map(x => x(0)-x(1)).toArray.reverse).pipe((_, ph) =>
            (seq, seq(0) - ph)
        )
    
    file.map(_.split(" ").map(_.toInt).pipe(slidingWindow(_))._2).sum

@main def main(day: Int): Unit =
    day match
        case 1 => 
            println("Day 1:")
            println("Part 1:\n" + day1part1(Source.fromFile("./Puzzle Inputs/day1.txt").getLines))
            println("Part 2:\n" + day1part2(Source.fromFile("./Puzzle Inputs/day1.txt").getLines))
        case 2 =>
            println("Day 2:")
            println("Part 1:\n" + day2part1(Source.fromFile("./Puzzle Inputs/day2.txt").getLines))
            println("Part 2:\n" + day2part2(Source.fromFile("./Puzzle Inputs/day2.txt").getLines))
        case 3 =>
            println("Day 3:")
            println("Part 1:\n" + day3part1(Source.fromFile("./Puzzle Inputs/day3.txt").getLines))
            println("Part 2:\n" + day3part2(Source.fromFile("./Puzzle Inputs/day4.txt").getLines))
        case 4 =>
            println("Day 4:")
            println("Part 1:\n" + day4part1(Source.fromFile("./Puzzle Inputs/day4.txt").getLines))
            println("Part 2:\n" + day4part2(Source.fromFile("./Puzzle Inputs/day4.txt").getLines))
        case 5 =>
            println("Day 5:")
            println("Part 1:\n" + day5part1(Source.fromFile("./Puzzle Inputs/day5.txt").getLines))
            println("Part 2:\n" + day5part2(Source.fromFile("./Puzzle Inputs/day5.txt").getLines))
        case 9 =>
            println("Day 9:")
            println("Part 1:\n" + day9part1(Source.fromFile("./Puzzle Inputs/day9.txt").getLines))
            println("Part 2:\n" + day9part2(Source.fromFile("./Puzzle Inputs/day9.txt").getLines))
        case x if x <= 25 && x >= 1 => println("I haven't made that day")
        case _ => println("Invalid day")
