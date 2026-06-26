def test_academic_redirect_without_login(client):
    r = client.get("/academic/")
    assert r.status_code in (302, 301)
