
import turtle


snowflake = turtle.Turtle()
snowflake.speed(1)


for i in range(1):
    for i in range(6):
        snowflake.forward(100)
        snowflake.forward(-40)
        snowflake.left(40)
        snowflake.forward(30)
        snowflake.forward(-30)
        snowflake.right(80)
        snowflake.forward(30)
        snowflake.forward(-30)
        snowflake.left(40)
        snowflake.forward(-60)
        snowflake.right(60)

