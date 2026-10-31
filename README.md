# api-lab
# API lab results

## Part 0
- Step 0.1, the number of pizza names: 18
- Step 0.3, status code of the request without a token: 401

## Defect report
- Title: Excluding all available tools returns HTTP 500
- Request: POST /api/pizza with excludedTools containing Knife, Pizza cutter and Scissors.
- Expected result: HTTP 400 with a JSON error message.
- Actual result: HTTP 500 with an empty response body.
- Severity: Medium. The API does not handle an impossible request gracefully.

## Part B

1. API tests can find problems in communication between the client and server,
   incorrect HTTP status codes, and problems with stored data.
   A unit test with stubs cannot fully check the real server and database.
   Unit tests are still useful because they are faster and help locate errors
   in individual functions.

2. Each test creates its own user to keep test data independent and prevent
   changing other users' ratings. In Project 2, I will create separate test
   accounts and only create, update, or delete data belonging to my tests.

3. The tests use one session because QuickPizza uses a load balancer and
   the session keeps its cookies. Without the same session, requests may
   reach different servers and login can fail.

4. The block that excludes all three tools revealed the defect. The API
   returned HTTP 500 with an empty body instead of HTTP 400 with a JSON
   error message. A 500 response is harder for an application to handle
   because it does not explain the invalid request. The test stays as xfail
   to document the known defect and detect when it is fixed.

5. Base choice coverage needs 9 tests:
   1 base test + 2 other C1 blocks + 3 other C2 blocks
   + 1 other C3 block + 2 other C4 blocks = 9 tests.
   All combinations coverage needs 3 x 4 x 2 x 3 = 72 tests.

6. The status codes from Step A4 were:
   - Read: [fill in your actual status code]
   - Update: [fill in your actual status code]
   - Delete: [fill in your actual status code]

   I expect all three requests to be refused because a user should not
   access another user's rating. A different 4xx code is not necessarily
   a defect if the API correctly refuses the request and the owner's
   rating remains unchanged.

7. The made-up token returned: [fill in the actual response].
   This should be investigated because accepting an invalid token could
   allow an unauthorised person to read private data on a real system.
   I only used the token to read ratings.

8. An API test checks status codes, response data and server behaviour
   directly. A test through web pages can check the visual layout,
   buttons and user experience, which an API test cannot check.

   # API Testing Lab

Course: ITCS386 - Software Verification and Validation

## Project Description

This project tests the QuickPizza API using Python, requests and pytest.
The tests check API responses, status codes, authentication, ratings,
input validation and user permissions.

## Requirements

- Python 3.10 or newer
- pytest
- requests
- pytest-html

## Installation

Clone this repository and open the project folder.

Create a virtual environment:

```bash
python -m venv .venv