def about_test(client):
    response = client.get("/about")
    assert response.status_code == 200
