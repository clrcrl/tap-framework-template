# tap-framework Template

This [cookiecutter](https://github.com/cookiecutter/cookiecutter) template is used in conjunction with [tap-framework](https://github.com/fishtown-analytics/tap-framework) to rapidly prototype Singer taps that use (sensible) REST APIs.

Now, I know what you're thinking, a template on top of a framework on top of a spec? That's too many layers of abstraction! And honestly, I couldn't agree more! However, after having built two taps and fussing around with a lot of copy/paste, I decided to go ahead with this.

These instructions assume you know a little bit about python — if something is confusing, please get in touch with me :).

## How to prototype a Singer tap

#### 1. Get to know the API you're using.

For example:
- Read the API docs to understand the main endpoints
- Generate credentials
- Use [Postman](https://www.postman.com/) or a similar tool to send a successful request using those credentials — this helps you understand how to work with the API. It's also worth learning:
    - How to get to the second page of results
    - How to change the number of items per request (and what the limit is)

#### 2. Create a new python virtual environment for cookiecutter
Name it cookiecutter and then `pip install cookiecutter`.

Activate the virtual environment.


#### 3. Create a new tap template and `cd` into it

From within the `cookicutter` virtualenv:
  - `pip install cookiecutter`
  - `cookiecutter gh:clrcrl/tap-framework-template`

A series of prompts will ask you for some details about your project. Values within `[]`s indicate the default — hit `return` to use that value.

A new directory should be created named `tap-<my-tap>` — `cd` into it.

Here's an example for [Ticket Tailor](https://developers.tickettailor.com/#ticket-tailor-api)
```bash
(tap-ticket-tailor-dev) $ cookiecutter gh:clrcrl/tap-framework-template
data_source [e.g. Ticket Tailor]: Ticket Tailor
project_name [tap-ticket-tailor]:
package_name [tap_ticket_tailor]:
python_class_prefix [TicketTailor]:
api_base_url [e.g. https://api.tickettailor.com/v1/]: https://api.tickettailor.com/v1/
endpoints_csv [e.g. events,issued_tickets,orders]: events,issued_tickets,orders
author_name [e.g. Alice Smith]: Claire Carroll
author_email [e.g. alice@gmail.com]: claire@clrcrl.com
```

And one for [Orbit](https://docs.orbit.love/reference):

```bash
(tap-orbit-dev) $ cookiecutter gh:clrcrl/tap-framework-template
data_source [e.g. Ticket Tailor]: Orbit
project_name [tap-orbit]:
package_name [tap_orbit]:
python_class_prefix [Orbit]:
api_base_url [e.g. https://api.tickettailor.com/v1/]: https://app.orbit.love/api/v1/dbt/
endpoints_csv [e.g. events,issued_tickets,orders]: activities,members
author_name [e.g. Alice Smith]: Claire Carroll
author_email [e.g. alice@gmail.com]: claire@clrcrl.com
```

#### 4. Create another virtual environment for your tap

Name it `tap-<my-tap>-dev` and activate it (or set it as the default virtualenv when working in the `tap-<my-tap>` directory).

Install the template as a command line utility
`pip install -e .`

Check the installation has worked by running: `tap-<my-tap> --help`:
```
$ tap-ticket-tailor --help
usage: tap-ticket-tailor [-h] -c CONFIG [-s STATE] [-p PROPERTIES]
                        [--catalog CATALOG] [-d]

optional arguments:
 -h, --help            show this help message and exit
 -c CONFIG, --config CONFIG
                       Config file
 -s STATE, --state STATE
                       State file
 -p PROPERTIES, --properties PROPERTIES
                       Property selections: DEPRECATED, Please use --catalog
                       instead
 --catalog CATALOG     Catalog file
 -d, --discover        Do schema discovery
```


#### 5. Update authorization keys
(This depends on the API that you're working with)

- Check the `config.json.example` file, and update it for the authentication key names needed for this API (don't put your own credentials in — this file just helps other developers)
- Create your own `config.json` and populate it with your credentials
- Update the required keys in `tap_<my_tap>/__init__.py`:

```py
args = singer.utils.parse_args(required_config_keys=["token"])
```

#### 6. Populate endpoint schemas

Populate each `schemas/<endpoint>.json` file with a jsonschema. Some APIs are kind, and make the jsonschema available (also worth checking the Dev Console in chrome to see if there's a request to get this file). If not, you can either:
- Manually write it from the API docs
- Use this [online tool to infer schemas](https://jsonschema.net/home).

If you're unfamiliar with jsonschemas, check out some [existing](https://github.com/fishtown-analytics/tap-orbit/tree/master/tap_tickettalor/schemas) [taps](https://github.com/fishtown-analytics/tap-orbit/tree/master/tap_orbit/schemas).


#### 7. Generate catalog.json
As per your tap's README, run the following:
```
{{ cookiecutter.project_name }} -c config.json --discover | jq '.streams[].metadata[0].metadata.selected = true' > catalog.json
```

Or simply:
```
make discover_and_select
```
Just for fun, try to use this generated catalog to see if the tap works:
```
{{ cookiecutter.project_name }} -c config.json --catalog catalog.json
```
You'll likely hit an error since we haven't adjusted the tap for your API

#### 8. Implement API-specific request logic
Every API has a different way of sending a request — to handle this, you'll be writing code in `client.py` — there's scaffold code to be edited there. Things to be mindful of:
- How does authorization happen?
- How many items do you want to fetch at a time, and how is that specified?
- What other headers need to be sent through?

This is where having successful Postman requests comes in handy!

#### 9. Implement endpoint logic
Head over to `streams/base.py` and start to adjust to account for pagination logic. Iteratively attempt to run your tap, and debug.

By the end of this step, you should be getting successful runs of your tap


#### 10. Make the tap incremental
Left as an exercise for the reader
