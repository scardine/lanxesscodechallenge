# LANXESS Code Challenge

## Backend Engineer Assessment

This is my stab at the code challenge for a position at LANXESS.


## The Challenge

I received the following task:

> Build an interview calendar API.
>
> It's okay to only implement the API and skip UI altogether. It's also fine to skip the
authentication. The purpose is not to build a solid API but for you to demonstrate your coding
skills and engineering practices.
>
> There may be two roles that use this API, a candidate and an interviewer. A typical scenario
is when:
>
>  1. An interview slot is a 1-hour period of time that spreads from the beginning of any hour until
the beginning of the next hour. For example, a time span between 9am and 10am is a valid
interview slot, whereas between 9:30am and 10:30am it is not.
>
> 2. Each interviewer sets their own availability slot. For example, the interviewer Philipp is
available next week each day from 9am through 4pm without breaks and the interviewer Sarah
is available from 12pm to 6pm on Monday and Wednesday next week, and from 9am to 12pm
on Tuesday and Thursday.
>
> 3. Each candidate sets their own requested slots for the interview. For example, the candidate
Carl is available for the interview from 9am to 10am any weekday next week and from 10am
to 12pm on Wednesday.
>
> 4. Anyone may then query the API to get a collection of periods of time when it's possible to
arrange an interview for a particular candidate and one or more interviewers. In this example,
if the API is queries for the candidate Carl and interviewers Philipp and Sarah, the response
should be a collection of 1-hour slots: from 9am to 10am on Tuesday, from 9am to 10am on
Thursday.


## Pre-requisites

* **Docker:** this document assumes you have docker (and docker-compose) working. This was tested on a Macbook pro with
Docker Engine version 18.03.1-ce and Docker Compose version 1.21.1.

* **Git:** you need git in order to clone the repo.

## Install

**WARNING:** This setup is for a local development environment meant to run on a workstation. 
**Do not publish this on a public Internet server unless you know the security implications.**

* Clone the repo:

    $ git clone https://github.com/scardine/lanxesscodechallenge.git  
    $ cd lanxesscodechallenge
    
* Build the container images:

    $ docker-compose build
    
* Run the contaners:

    $ docker-run
    
If everything went OK you will be able to access the API at http://localhost:8000/


## Troubleshooting

* check if your firewall is blocking TCP port 8000

* check if TCP port 8000 is in use by another application

* if there is an error, copy & paste it or take an screenshot and send to pauloscardine@seade.gov.br
 and I will help you diagnose and fix the problem - I will do my best to answer in a timelly fashion 
 but if you are in a hurry call +5511989634414. I'm in Brazil, UTC -3 (-2 in the summer), check 
 [XKCD Now](https://xkcd.com/1335/) in order to check for business hours (I may not answer unless
 it is yellow in South America).
 
 
## The endpoints

There is a browseable interface at http://localhost:8000/api/ for exploration and tests. Also, every 
endpoing listed there accepts the OPTIONS method and will return a JSON description of the endpoing 
suitable for automated bindings.


### Actors (/api/actors/)

Actors are either candidates or interviewers. This endpoint accepts:

* GET: list actors
* POST: create a new actor

Whit an actor ID appended to the URL (i.e. /api/actors/1/) it accepts:

* GET: retrieve a particular actor
* PUT/PATCH: update
* DELETE: removes an actor

Sample call from the command line:

    $ curl -H "Accept: application/json; indent=4" 'http://localhost:8000/api/actors/1/'
    
Result:
    
    {
        "id": 1,
        "slots": [
            ["monday", 9],
            ["monday", 10],
            ["monday", 11]
        ],
        "name": "Philipp",
        "role": "interviewer"
    }

### Availability (/api/availability)

This endpoints take one or more "actor" IDs and returns time slots suitable for a meeting where
all actors can participate. An slot is represented by the weekday name and the start hour.

* GET: list of available 1h slots where all attendees are free

Sample call from the command line:

    $ curl -H "Accept: application/json; indent=0" \
           'http://localhost:8000/api/availability/?id=1&id=2'
 
Result:
 
    [["monday", 9],["monday", 10],]


## Tests

From the project folder run:

    docker-compose exec web python3 manage.py test 
    
Expected output:

    Creating test database for alias 'default'...
    System check identified no issues (0 silenced).
    ..
    ----------------------------------------------------------------------
    Ran 2 tests in 0.459s

    OK
    Destroying test database for alias 'default'...
    
    
## Loading sample data

In order to play with the API you may want to load some sample data. From the project folder run:

    docker-compose exec web python3 manage.py loaddata api/fixtures/sample_data.json


## Contributing

### Code Style

We follow [PEP8](https://www.python.org/dev/peps/pep-0008/) with a single difference: we use 120 
character lines instead of 80 (lets not waiste our ultra-wide monitors and retina displays). Use
a linter and make sure your patches have no linter warnings.

### Documentation and Tests

If you are fixing a bug, please include a test to defend against it in the future. If you are
implementing a new feature documentation is mandatory and for tests use your wisdom - no need to
test if 2 + 2 is 4 but it is nice to write some tests in order to make sure your code does what 
you say it does.



