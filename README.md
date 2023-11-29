# Flask Money Transfer Project

This is a sample project for a money transfer application using the Flask framework.

## Environment Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/ze-fernando/SimplePayment-API

   cd SimplePayment-API
   
   pip install requirements.txt
   ```
2. Create and activate a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```
4. Configure environment variables (optional, depending on your setup):

    ```bash
    export FLASK_APP=run.py
    export FLASK_ENV=development  
    ```
5. Start the Flask server:

    ```bash
    flask run # or python run.py
    ```
The application will be available at http://localhost:5000.

API Endpoints
- POST /transfer
- Performs a money transfer between users.

Expected payload:
```json
{
  "sender": 1,
  "receiver": 2,
  "amount": 50.0,
  "description": "Optional transaction description"
}
```
Returns a JSON response indicating the result of the transaction.
- POST /users
- Register your user in app

```json
{
   "name": "Joseph Shell",
   "cpf": "14725836900",
   "email": "shelljoseph@email.com",
   "balance": 1580,
   "type": "common",
   "password": "h-a-s-h-1-2-3"

}
```
Returns a JSON response indicating the result of the register.

### Contribution
Feel free to contribute improvements, bug fixes, or new features. Open an issue or submit a pull request!
