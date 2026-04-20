# Title

![Image]()

|Date |       |
|:----|:------|
|19 April 2026 |Assigned |
|27 April 2026 |Due |
|Progress        |[![Grade](../../actions/workflows/main.yml/badge.svg?branch=main)](../../actions/workflows/main.yml) |

![](https://img.shields.io/badge/assignment-lab-yellow.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAB2AAAAdgFOeyYIAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAa9JREFUOI2Vkk1IVGEUhp9zvd7bfKNz51JojQWZkARmI2qCULjrbxkTs4nCVRC0LHeuZhGzDFqEKzcGs2vXxhatAxUhUTQt1I0mNkzZ/NzjYrBmplFu7+bjvOfl4ZyPIzTRtZR2BcKVWs9SPs/nZLMxazcDBBajmQkyXowYwMY2X7OvyAK5UADH4kM0gokbOksBurnNSslltlnWamZ+mpGdwk+KAEGF8uo67tK07IYGAKhU37Ly67jMiYA/ASGSL3DqvwDJxxp3bVoAygE/oobiYEq90AD9TV+snXYAxybm+5QqQl9oQOIs48bBB3BbaL1/iyHP51EoQDKtYy+eckfkrxe1sZ+Mk0ymdexEwEBaEw9TvPQMHVrbELh8nuF7t3k+kNZEbavukEau87q3hzNbu2zs7JH/vkf+XAfexS4uWBbujREuvZ9lCrhbw67q6gO9+SbLO+NQ99sKWiiyXzzgwEQwW/usTWZ4tvBWPtZPYDFoWqu33zC9tDnEcaq130avwhBQDxBhfnGduc7TxBshR6oowfIa36yAuX9WAOhPabcKPccBAERZXcjJl6P6EOkCeLyZu19AAAAAAElFTkSuQmCC)

Pulling together all of our learning this semester, your team will complete an obstacle course of sorts. At a high level, this task is to measure five (5) "obstacles" denoted by blue painter's tape spread throughout Alden Hall. These obstacles are challenges which require you to measure the distance between a "starting line" and a flat standing surface.

The team that gets closest to the actual numbers measured in `feet` and `meters` (within `1%`) wins!

## Learning Objectives

This assignment addresses the following course learning objective(s):

1. Apply Python programming fundamentals to execute and explain computer code that implements interactive, novel solutions to a variety of computable problems.
2. Implement code consistent with industry-standard practices using professional-grade integrated development environments (IDEs), command-line tools, and version control systems.
3. Analyze and suggest revisions to existing Python language code to add functionality or repair defects.
4. Evaluate the practical and ethical implications of writing computer code and discuss the contexts, perceived effects, and impacts exerted on and by computer code as a cultural force or artifact.
5. Design, describe, and implement original projects incorporating industry-standard practices and Python language fundamentals.

## Pinout Diagram

> [!NOTE]
> This assignment does not require LEDs.

![]()

The above graphic is a `pinout diagram`: a description of how to wire a _physical computing_ project. Match the above diagram with the following components:

* push button
* Raspberry Pi Pico
* `6` wires
* `2` breadboards
* `1` resistor
* ultrasonic sensor

|Pins |Purpose |
|:----|:-------|
|`15` |Button  |
|`13` |Sensor "echo" |
|`12` |Sensor "trigger" |

#### Detour into ultrasonic sensors

The sensor used for this assignment is an _ultrasonic_ sensor: one that sends out "pings" in order to hear "echoes" back. The time between the ping and the echo indicates how much distance there is between the sensor and the nearest object. If you're thinking about [bats, or other animals that use echolocation](https://en.wikipedia.org/wiki/Animal_echolocation), you're on the right wavelength. 

One thing to think about in this lab is the time between trigger sounds and echos: does adjusting it up or down create a better result?

> [!IMPORTANT]
> The above writing is _critical_ to the code. We address specific parts during our programs. Make sure it matches. If you have questions, ask a TL or the instructor!

## Summary of the problem

> [!IMPORTANT]
> In order to run the program in this lab, you'll need to do the following when you've made the appropriate changes:
> ```
> uv run mpremote cp src/sensor.py :
> uv run mpremote cp src/secrets.py :
> uv run mpremote cp src/measurements.py :
> uv run mpremote cp .env :
> ```
> As you will make changes in this file to create a functional and accurate program, you'll need to upload the files you change to the device!

> [!NOTE]
> It's up to you to finish and demonstrate a cohesive testing plan. This includes updating tests in the `tests/test_proxsensor.py` file.

The lab consists of three (`3`) parts:

* a `sensor` object which captures the value of the Pico ultrasonic sensor
* a `measurements` object which takes the output of the sensor and calculates distances from it
* a `main` (driver) file that controls the interaction between the `measurements` and `sensor`, while guiding the flow of the program
  * in addition, `main` should upload values to an API in order to figure out if you're close to any of the measurements (https://dev.chompe.rs/submit-measure)
  * the API takes `1` parameter: `value` which is the distance from an object in `feet`

  ### `main`

`main` operates a loop until the `button` is pressed, at which point it takes a sensor reading and outputs the distance from an object in `centimenters` and `feet` in a format matching:
```
Object is:
* 1.67 feet away
* 0.51 meters away
```

This portion of the program also connects to the internet and uploads a measurement to the remote API. _This connection is done via the Pico!_ We will need to create a file called `.env` to make this happen.

* create a file called `.env` in the main folder of the lab
* add two values to the file:
```
SSID=
PASS=
```
We will fill these in with details provided in class. These are network secrets, so we won't post them in GitHub!

### `sensor`

This object has two purposes: start the `trigger` ping and wait for `echo`es to return. Once you have the value, like everything in this course, it's less-than-straightforward. 

### `measurements`

Use the following formula to convert from a reading to a distance in centimeters.

$$ \frac{\frac{reading}{2}}{29.1} $$

Notice that the program wants `feet` and `meter`s. How do we get that?

## Assignment procedure

> [!IMPORTANT]
> As a team assignment, this repository _does not allow_ direct `commit`s to `main`. Here you'll have to use `branch`es and reviews to ensure that the project functions and is generally well understood by the team. 
>
> In practice, this means that everyone _must_ `branch` their changes _and_ that each `Pull Request` requires `2` reviews before it can be `merge`d.

## Evaluation

> [!NOTE]
> To grade this lab, use the `uv run gatorgrade` command.

Labs in this course are each worth `5` points. You are awarded different levels of points using the following rubric:

|Component|Value |
|:--------|:-----|
|Programming|2   |
|Code Review|2   |
|Writing    |1   |
|**Total**  |**5**|

### Programming

Your programming will be evaluated on the following characteristics:

* Program reflects startup expectations in `main`
* Program reads correct temperature
* Program displays relative temperature correctly using `LED`s

#### Expected output

The output for this program relies on external LEDs to validate outputs/outcomes.

#### Code review

Either a Technical Leader `TL` or the instructor can perform a code review with you. This _must_ be done before the due date for the assignment. You may accomplish this during a lab session, TL office hours, or during the instructor's office hours. Successful completion of this review (and an accompanying successful outcome) will earn points toward the code review portion of the assignment.

> [!IMPORTANT]
> Teams must complete the code review _together_ for this lab. Students not present for the code review will not recieve credit for it.

#### Writing

Students are expected to finish a [summary document](docs/summary.md). This is a Markdown file containing questions. All questions must be answered fully. Typically, this means a word count is assessed. 

For this assignment, the minimum required word count is `150`.