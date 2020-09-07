This cookie cutter template is used in conjunction with [tap-framework]() to rapidly prototype Singer taps that use REST APIs.

## How to prototype a Singer tap

1. Get to know the API you're using.

For example:
- Read the API docs to understand the main endpoints
- Generate credentials
- Use [Postman](https://www.postman.com/) or a similar tool to send a successful request using those credentials — this helps you understand how to work with the API

2. Create a new tap template

< to do: instructions for copying this >



3. Update the tap template for your use case, in particular:


**Authorization**:
Check the `config.json.example` file, and update it for the authentication key names needed for this API (don't put your own credentials in — this file just helps other developers)

< to do >

**Endpoint schemas**:
Populate each `schemas/<endpoint>.json` file with a jsonschema. Some APIs are kind, and make the jsonschema available (also worth checking the Dev Console in chrome to see if there's a request to get this file). If not, you can either:
- Manually write it from the API docs
- Use the [`singer-infer schema` helper tool](https://github.com/singer-io/singer-tools#singer-infer-schema) to infer the schema

**Response codes:**
The BaseClient

4. Make the tap incremental
Left as an exercise for the reader
