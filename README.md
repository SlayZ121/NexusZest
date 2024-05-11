# Online Trading System

## Description
This is an online trading system where users can register, buy items from the market, and sell items they own. The system includes user authentication to ensure security and privacy.

## Features
- **User Registration:** New users can create an account by providing their details such as username, email, and password.
- **User Authentication:** Users are required to log in with their credentials to access the system.
- **Buying Items:** Users can browse the market and purchase items listed by other users.
- **Selling Items:** Users can list items they own for sale on the platform.
- **User Profile:** Each user has a profile page where they can view their account information and transaction history.

## Technologies Used
- **Frontend:** HTML, CSS, JavaScript (with Bootstrap for styling)
- **Backend:** Python (Flask framework)
- **Database:** SQLite 3 (with SQLAlchemy for database interactions)

## Installation
1. Clone the repository:
    ```
    git clone <repository-url>
    ```
2. Install dependencies:
    ```
    cd online-trading-system
    pip install -r requirements.txt
    ```

3. Set environment variables:
    - Create a `.env` file in the root directory.
    - Add the following environment variables:
        ```
        PORT=3000
        DATABASE_URL=sqlite:///path/to/database.db
        SECRET_KEY=<your-secret-key>
        ```

4. Set up the database:
    - Initialize the SQLite database by running the following command in the terminal:
        ```
        flask db init
        ```
    - Create the initial migration:
        ```
        flask db migrate -m "Initial migration"
        ```
    - Apply the migration to the database:
        ```
        flask db upgrade
        ```

5. Start the Flask server:
    ```
    python app.py
    ```

## Usage
1. Register a new account by providing your details.
2. Log in with your credentials.
3. Browse the market to find items you want to buy.
4. To sell items:
   - Go to your profile page.
   - Select the option to list a new item for sale.
5. Complete transactions by confirming purchases and sales.

## Contributing
Contributions are welcome! If you have any suggestions or improvements, feel free to submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Authors
- [Your Name](https://github.com/your-username)
