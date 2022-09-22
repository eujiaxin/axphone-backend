# axphone-backend 

[Django REST Framework](https://www.django-rest-framework.org/) has been used to create a simple CRUD API for the phonebook website **AxPhone**. 

# Structure
In the RESTful API, endpoints (URLs) define the structure of the API and how end users can interact with the frontend interface and access data from the application using HTTP methods - GET, POST, PATCH, DELETE.  

For AxPhone, there is a single resource/model `Contacts` to store relevant details of every contact.

| Endpoint        | HTTP Method | CRUD Method | Result                                |
|-----------------|-------------|-------------|---------------------------------------|
| `contacts/`     | GET         | READ        | Get all contacts to show in home page |
| `contacts/:id/` | GET         | READ        | Get a single contact for edit details |
| `contacts/`     | POST        | CREATE      | Create a new contact                  |
| `contacts/:id/` | PATCH       | UPDATE      | Update an existing contact            |
| `contacts/:id/` | DELETE      | DELETE      | Delete an existing contact            |

<br/>

Example data retrieved from sending a GET request to the `contacts/` endpoint:
```json
[
    {
        "id": 1,
        "name": "Lucy",
        "phone_number": "0123456789"
    },
    {
        "id": 2,
        "name": "Kiwi",
        "phone_number": "01987654321"
    }
]
```

<br>

*The frontend repository written in React can be found [here](https://github.com/heheheejin/axphone-frontend).*
