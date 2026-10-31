import pytest

STARS_ERROR = "number of stars must be between 1 and 5 (inclusive)"


# Base choice: 3 stars as a whole number, a real pizza, and the user's token.
def test_base_choice_is_saved(api, auth, pizza_id):
    new = {"pizza_id": pizza_id, "stars": 3}

    res = api.post("/api/ratings", json=new, headers=auth)

    assert res.status_code == 201
    assert res.json()["stars"] == 3
    assert res.json()["pizza_id"] == pizza_id


# C1: A number of stars below 1 or above 5 is refused.
@pytest.mark.parametrize("stars", [0, 6])
def test_stars_out_of_range(api, auth, pizza_id, stars):
    new = {"pizza_id": pizza_id, "stars": stars}

    res = api.post("/api/ratings", json=new, headers=auth)

    assert res.status_code == 400
    assert res.json() == {"error": STARS_ERROR}


# C2: Decimal stars are refused.
def test_decimal_stars_is_refused(api, auth, pizza_id):
    new = {"pizza_id": pizza_id, "stars": 3.5}

    res = api.post("/api/ratings", json=new, headers=auth)

    assert res.status_code == 400
    assert "error" in res.json()


# C2: Text stars are refused.
def test_text_stars_is_refused(api, auth, pizza_id):
    new = {"pizza_id": pizza_id, "stars": "3"}

    res = api.post("/api/ratings", json=new, headers=auth)

    assert res.status_code == 400
    assert "error" in res.json()


# C2: Missing stars are refused.
def test_missing_stars_is_refused(api, auth, pizza_id):
    new = {"pizza_id": pizza_id}

    res = api.post("/api/ratings", json=new, headers=auth)

    assert res.status_code == 400
    assert "error" in res.json()


# C3: A rating for a pizza that does not exist is refused.
def test_nonexistent_pizza_is_refused(api, auth):
    new = {"pizza_id": 999999999, "stars": 3}

    res = api.post("/api/ratings", json=new, headers=auth)

    assert res.status_code == 400
    assert "error" in res.json()


# C4: A request without a token is refused.
def test_missing_token_is_refused(api, pizza_id):
    new = {"pizza_id": pizza_id, "stars": 3}

    res = api.post("/api/ratings", json=new)

    assert res.status_code == 401
    assert res.json() == {"error": "authentication failed"}


# C4: A request with a short token is refused.
def test_short_token_is_refused(api, pizza_id):
    new = {"pizza_id": pizza_id, "stars": 3}
    short_auth = {"Authorization": "token 123"}

    res = api.post("/api/ratings", json=new, headers=short_auth)

    assert 400 <= res.status_code <= 499