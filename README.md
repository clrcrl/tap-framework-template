# [WIP] tap-framework Template

This [cookiecutter](https://github.com/cookiecutter/cookiecutter) template is used in conjunction with [tap-framework](https://github.com/fishtown-analytics/tap-framework) to rapidly prototype Singer taps that use REST APIs.

Now, I know what you're thinking, a template on top of a framework on top of a spec? That's too many layers of abstraction! And honestly, I couldn't agree more! However, after having built two taps and fussing around with a lot of copy/paste, I decided to go ahead with this.

These instructions assume you know a little bit about python — if something is confusing, please get in touch with me :).

## How to prototype a Singer tap

#### 1. Get to know the API you're using.

For example:
- Read the API docs to understand the main endpoints
- Generate credentials
- Use [Postman](https://www.postman.com/) or a similar tool to send a successful request using those credentials — this helps you understand how to work with the API

#### 2. Create a new python virtual environment
Name it something like `tap-<my-tap>-dev` (replacing `<my-tap>` with the name of your tap).


#### 3. Create a new tap template

From within the virtualenv:
  - `pip install cookiecutter`
  - `cookiecutter gh:clrcrl/tap-framework-template`

A series of prompts will ask you for some details about your project. Values within `[]`s indicate the default — hit `return` to use that value.

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

Now, you should have a pre-filled template in your directory.

#### 4. Install the template as a command line utility
`pip install -e .`

Check this works by running: `tap-<my-tap> --help`:
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


#### 5. Update the tap template for your use case, in particular:

The template can only take you so far.

**Authorization**:
Check the `config.json.example` file, and update it for the authentication key names needed for this API (don't put your own credentials in — this file just helps other developers)

Then, you'll likely need to implement your own version of the `make_request` method that is part of tap-framework. To do this:
1. View the code in [tap-framework](https://github.com/fishtown-analytics/tap-framework/blob/master/tap_framework/client.py#L16)
2. Copy it into _your_ `<MyTap>Client` and adjust the code based on the API that you're using

**Endpoint schemas**:
Populate each `schemas/<endpoint>.json` file with a jsonschema. Some APIs are kind, and make the jsonschema available (also worth checking the Dev Console in chrome to see if there's a request to get this file). If not, you can either:
- Manually write it from the API docs
- Use the [`singer-infer schema` helper tool](https://github.com/singer-io/singer-tools#singer-infer-schema) to infer the schema

If you're unfamiliar with jsonschemas, check out some [existing](https://github.com/fishtown-analytics/tap-orbit/tree/master/tap_tickettalor/schemas) [taps](https://github.com/fishtown-analytics/tap-orbit/tree/master/tap_orbit/schemas).


**Pagination logic:**
TODO (But check you're probably going to be working in `streams/base.py` to implement pagination logic)

#### 6. Attempt to run the tap
At this point, use the tap's README to try to follow the instructions on how to use the tap

#### 7. Make the tap incremental
Left as an exercise for the reader
