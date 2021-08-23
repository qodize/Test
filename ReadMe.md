<h3>install venv</h3>

py -m venv venv<br>
source venv\Scripts\activate<br>

<h3>install requirements</h3>
pip install -r requirements.txt

<h3>Provide Database name</h3>
go to .env and set DBNAME variable<br>
(by default DBNAME=testing)

<h3>Run migrations</h3>
cd onlineshop
py manage.py makemigrations
py manage.py migrate

<h3>Run server</h3>
py manage.py runserver

<h3> curl commands </h3>
<h4>Get all products</h4>

curl 127.0.0.1:8000/api/products/

<h4>Filter products by name</h4>

curl -X GET
-H 'Content-Type: application/json'
-d '{"filter_by": "name", "value": "some name"}'
127.0.0.1:8000/api/products/

This will return you all products with name "some name"

<h4> Filter products by parameter </h4>

curl -X GET
-H 'Content-Type: application/json' 
-H 'Accept: application/json' 
-d '{"filter_by": "param1", "value": "0"}' 
127.0.0.1:8000/api/products/

This will return you all products which have "param1": "0" in parameters

<h4> Get product by id </h4>
curl -X GET 
-H 'Content-Type: application/json' 
-H 'Accept: application/json'
127.0.0.1:8000/api/products/3

This will return you product with id 3

<h4> Create new product </h4>
curl -X POST
-H 'Content-Type: application/json'
-H 'Accept: application/json' 
-d '{
    "name": "some product",
	"description": "Lorem ipsum dolor sit amet",
	"params": {
		"param1": "some parameter",
		"param2": "other parameter"
	}
}' 
127.0.0.1:8000/api/products/

<h3> Testing scenario </h3>

<h4> Create new product </h4>

curl -X POST
-H 'Content-Type: application/json'
-H 'Accept: application/json' 
-d '{
    "name": "First Product",
	"description": "Lorem ipsum dolor sit amet",
	"params": {
		"param1": "300 bucks",
		"param2": "0"
	}
}'

curl -X POST
-H 'Content-Type: application/json'
-H 'Accept: application/json' 
-d '{
    "name": "Second Product",
	"description": "Lorem ipsum dolor sit amet",
	"params": {
		"param1": "200 bucks",
		"param2": "2"
	}
}'

<h4> Check if these two products were created </h4>

curl 127.0.0.1:8000/api/products/

<h4> Find First Product by parameter </h4>

curl -X GET
-H 'Content-Type: application/json' 
-H 'Accept: application/json' 
-d '{"filter_by": "param1", "value": "300 bucks"}' 
127.0.0.1:8000/api/products/

This will return you name of the product and its id
Output:
{
"id": 1,
"name": "First Product"
}

<h4> Get details of product by its id </h4>

curl -X GET 
-H 'Content-Type: application/json' 
-H 'Accept: application/json'
127.0.0.1:8000/api/products/1


Thank you
