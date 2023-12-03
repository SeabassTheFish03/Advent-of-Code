import scala.io.Source
import scala.util.matching.Regex._

def printPass[A](obj: A): A =
	try
		println(obj.toString)
	catch
		case _ => println("Object cannot be printed")
	obj

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
				/* So close, but need to replace */
				Source.fromFile("./Puzzle Inputs/day1.txt").getLines.toList.map(line =>
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
		case _ => println("Invalid day")