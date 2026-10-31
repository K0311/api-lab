import pytest


# Updating stars checks values below, at and above the valid boundaries.
@pytest.mark.parametrize(
    "stars, expected_status",
    [
        (0, 400),
        (1, 200),
        (5, 200),
        (6, 400)
    ]
)
def test_update_rating_boundary_values(
    api, auth, rating, stars, expected_status
):
    path = f"/api/ratings/{rating['id']}"

    res = api.put(path, json={"stars": stars}, headers=auth)

    assert res.status_code == expected_status

    # Read the rating again to check whether the update was saved or refused.
    check = api.get(path, headers=auth)
    assert check.status_code == 200

    if expected_status == 200:
        assert check.json()["stars"] == stars
    else:
        assert check.json()["stars"] == 3