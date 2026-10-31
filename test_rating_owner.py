# Another user cannot read the owner's rating.
def test_other_user_cannot_read_rating(api, auth, rating, other_auth):
    path = f"/api/ratings/{rating['id']}"

    res = api.get(path, headers=other_auth)

    assert 400 <= res.status_code <= 499

    # The owner can still read the unchanged rating.
    owner_check = api.get(path, headers=auth)
    assert owner_check.status_code == 200
    assert owner_check.json()["stars"] == 3


# Another user cannot update the owner's rating.
def test_other_user_cannot_update_rating(api, auth, rating, other_auth):
    path = f"/api/ratings/{rating['id']}"

    res = api.put(
        path,
        json={"stars": 1},
        headers=other_auth
    )

    assert 400 <= res.status_code <= 499

    # The owner must still see the original rating.
    owner_check = api.get(path, headers=auth)
    assert owner_check.status_code == 200
    assert owner_check.json()["stars"] == 3


# Another user cannot delete the owner's rating.
def test_other_user_cannot_delete_rating(api, auth, rating, other_auth):
    path = f"/api/ratings/{rating['id']}"

    res = api.delete(path, headers=other_auth)

    assert 400 <= res.status_code <= 499

    # The owner can still read the rating after the refused delete.
    owner_check = api.get(path, headers=auth)
    assert owner_check.status_code == 200
    assert owner_check.json()["stars"] == 3