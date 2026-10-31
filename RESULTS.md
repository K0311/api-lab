# API lab results

## Part 0

- Step 0.1, the number of pizza names: 18
- Step 0.3, status code of the request without a token: 401
- Step 0.4, the name of your pizza: [Write the actual pizza name from your API response]
- Step 0.12, results of the three runs without a session (optional): [Write the results if performed, otherwise Not performed]
- Step 0.16, blocks of "how many of the three tools are excluded": 0 tools, 1 tool, 2 tools, and 3 tools.

## Defect report

- Title: Excluding all three available tools returns HTTP 500.
- Request: POST /api/pizza with excludedTools containing Knife, Pizza cutter, and Scissors.
- Expected result: HTTP 400 with a JSON error message explaining that the request cannot be fulfilled.
- Actual result: HTTP 500 with an empty response body.
- Severity: Medium, because the API does not handle an invalid request properly and does not provide a useful error message.

## Part A

- Step A4, status codes when the other user reads, changes and deletes:
  - Read: [Write actual status code]
  - Change: [Write actual status code]
  - Delete: [Write actual status code]

## Part B

1. API tests can find problems in communication between the client and the server, incorrect HTTP responses, and problems with stored data. Unit tests with stubs cannot fully test the real server and database. However, unit tests are still useful because they are faster and help find errors in individual functions.

2. Each test creates its own user with a new name to keep test data independent and prevent changing other users' ratings. In Project 2, I will also create separate test accounts and only create, update, or delete data belonging to my tests.

3. The tests use one session because QuickPizza uses a load balancer and the session keeps cookies. The cookies help the requests reach the same server. Without a session, requests may reach different servers and login can fail.

4. The block that excludes all three tools revealed the defect. The API returned HTTP 500 with an empty response body instead of HTTP 400 with a JSON error message. A 500 response is worse because the application does not receive a clear explanation of the problem. The test stays as xfail to document the known defect and detect when the API is fixed.

5. Base choice coverage needs 9 tests. There are 4 characteristics, and the number of tests is 1 base test plus 2 other blocks for C1, 3 other blocks for C2, 1 other block for C3, and 2 other blocks for C4. Therefore, 1 + 2 + 3 + 1 + 2 = 9 tests. All combinations coverage needs 3 x 4 x 2 x 3 = 72 tests.

6. The status codes from Step A4 were:
   - Read: [Write actual status code]
   - Change: [Write actual status code]
   - Delete: [Write actual status code]

   I expect all three requests to be refused because a user should not access or change another user's rating. Different 4xx status codes are not necessarily defects if the API correctly refuses the requests and the owner's rating remains unchanged.

7. The response from the made-up token was: [Write the actual response from your terminal].

   If an invalid token is accepted, it may be a security problem. On a real system, a stranger might be able to read private information without permission. I only used this token to read ratings and did not create or change any data.

8. An API test checks HTTP status codes, response data, and server behaviour directly. A test through web pages can check the visual layout, buttons, and user experience, which an API test cannot check.