import scala.io.Source
import scala.util.matching.Regex
import scala.util.matching.Regex._
import scala.util.chaining._

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
			def part1: Int =
				Source.fromFile("./Puzzle Inputs/day2.txt").getLines.map(line =>
					Map("red" -> 12, "green" -> 13, "blue" -> 14).pipe(maxMap => 
						"Game ([0-9]+): (.*)".r.findFirstMatchIn(line).map(matches =>
							matches.group(2).split("; ").map(mat =>
								"([0-9]+) (red|blue|green)".r.findAllMatchIn(mat).foldRight(true)((item, accum) =>
									(maxMap(item.group(2)) >= item.group(1).toInt) && accum
								)
							).foldRight(matches.group(1).toInt)((a, b) => if a then b else 0)
						).getOrElse(0)
					)
				).sum

			println("Day 2:")
			println("Part 1:\n"+
				/*((gameRegex: Regex) =>
					Source.fromFile("./Puzzle Inputs/day2.txt").getLines.toList.slice(0, 5).map(line =>
						line match
							case gameRegex(game_num, rest, _*) =>
								(extractorRegex: Regex =>
									rest.split(";").map(singleGame =>
										singleGame match
											/* %d blue/green/red, */
									)
									rest match
										case restRegex =>
								).apply("([0-9]+) (blue|green|red),?".r)
					)
				).apply("Game ([0-9]+): ([0-9]* .*;?)*".r)*/
				part1.toString
			)
		case _ => println("Invalid day")