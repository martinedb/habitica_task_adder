# Habitica Task Adder

A Python script for efficiently adding long or complex tasks—complete with checklists—to your Habitica To-Do list via the Habitica API.

---

## **Overview & Purpose**

**Habitica** is a gamified productivity platform that transforms your tasks and goals into RPG-style quests. This script streamlines the process of creating Habitica To-Do tasks, especially those requiring detailed checklists, by automating API interactions.

- **Purpose:**  
  Automate the creation of Habitica To-Do tasks with customizable checklists, saving time and ensuring consistency.
- **Benefits:**  
  - Reduces manual entry for repetitive or complex tasks.
  - Enables bulk or scripted task creation.
  - Empowers integration with other workflows or tools.
- **Habitica API Background:**  
  - RESTful API supporting standard HTTP methods (`GET`, `POST`, `PUT`, `DELETE`).
  - Common use cases: managing tasks, retrieving user stats, updating habits, and more.
  - Documentation: [Habitica API Reference](https://habitica.com/apidoc/)

---

## **Prerequisites**

- **Python Version:**  
  Python **3.6+** recommended.

- **Required Libraries:**  
  - [`requests`](https://pypi.org/project/requests/) (for HTTP requests)

- **Other Requirements:**  
  - **Habitica Account:** Sign up at [habitica.com](https://habitica.com/).
  - **API Credentials:**  
    - **User ID** (`HABITICA_USER_ID`)
    - **API Token** (`HABITICA_API_TOKEN`)
    - Generate at [User > Settings > API](https://habitica.com/user/settings/api)

---

## **Installation & Setup**

### 1. **Clone the Repository**

```bash
git clone https://github.com/martinedb/habitica_task_adder.git
cd habitica_task_adder
```

### 2. **Install Dependencies**

```bash
pip install requests
```

### 3. **Configure Environment Variables**

#### **Recommended: Use a `.env` File**

Create a file named `.env` in the project directory:

```env
HABITICA_USER_ID=your_habitica_user_id
HABITICA_API_TOKEN=your_habitica_api_token
```

Use [python-dotenv](https://pypi.org/project/python-dotenv/) for automatic loading (optional):

```bash
pip install python-dotenv
```
Add this to the script if using `python-dotenv`:
```python
from dotenv import load_dotenv
load_dotenv()
```

#### **Alternatively: Set Directly in Your Shell**

```bash
export HABITICA_USER_ID=your_habitica_user_id
export HABITICA_API_TOKEN=your_habitica_api_token
```

---

## **Usage Instructions**

### **Basic Execution**

Edit `habitica_task_adder.py` to customize your task:

```python
task = {
    "text": "Update my personal website",
    "type": "todo",
    "checklist": [
        {"text": "Add personal portfolio projects"},
        {"text": "Add headers to website"},
        {"text": "Add about me page"},
    ]
}
```

Then run:

```bash
python habitica_task_adder.py
```

If successful, you’ll see:
```
Task created successfully!
```
This new to-do list item with a checklist should be immediately reflected in your Habitica home page under "To-Do's"

### Screenshot of Habitica HomePage
<img width="493" height="290" alt="image" src="https://github.com/user-attachments/assets/158e2ff7-f070-44a5-a533-25148514580c" />

### **Customizing Tasks**

- **Task Name:** Change the `text` field.
- **Checklist:** Modify/add items within the `checklist` array.
- **Task Type:**  
  - Supported: `"todo"`, `"habit"`, `"daily"`, `"reward"`

### **Sample Input/Output**

**Sample Input:**
```python
task = {
    "text": "Write Blog Post",
    "type": "todo",
    "checklist": [
        {"text": "Draft outline"},
        {"text": "Write content"},
        {"text": "Proofread"},
        {"text": "Publish"}
    ]
}
```

**Sample Output:**
```
Task created successfully!
```

---

## **Authentication & Security**

- **Never hardcode API credentials** in your scripts or commit them to source control.
- Use **environment variables** or `.env` files (excluded via `.gitignore`).
- **Protect your API tokens:**  
  - Do **not** share tokens in screenshots, code samples, or public repositories.
- **Habitica API Rate Limits:**  
  - Be mindful of request quotas; excessive requests may lead to throttling or temporary bans (see [Habitica API docs](https://habitica.com/apidoc/)).

---

## **Error Handling & Troubleshooting**

### **Common Errors**

- **Invalid API Key/User ID:**
  ```
  Error 401: {'success': False, 'error': 'NotAuthorized', 'message': 'Missing or invalid API credentials.'}
  ```
  **Resolution:**  
  - Double-check your credentials and environment variable setup.

- **Network Issues:**
  ```
  Error 503: {'success': False, 'error': 'ServiceUnavailable', 'message': 'Server temporarily unavailable.'}
  ```
  **Resolution:**  
  - Check your internet connection or try again later.

### **Debugging Tips**

- Add verbose logging:
  ```python
  print(response.text)
  ```
- Use [requests logging](https://docs.python-requests.org/en/master/api/#logging).

---

### Extra Tip
For tasks that require extensively long checklists, ask an AI chatbot such as ChatGPT to immediately modify the code to incorporate a long list of tasks into the Habitica Task Adder.
That way, you don't have to manually add to-do items with long checklists.

## **Contributing & Support**

- **Bug Reports / Feature Requests:**  
  Open an [issue](https://github.com/martinedb/habitica_task_adder/issues).
- **Pull Requests:**  
  - Fork the repo, create a feature branch, submit a PR with clear description.
  - Follow Python best practices (PEP8, modular code).
- **Advanced Usage:**  
  - Refer to [Habitica API Documentation](https://habitica.com/apidoc/) for additional endpoints and options.

---

## **License & Disclaimer**

- **License:**  
  [MIT License](LICENSE)
- **Disclaimer:**  
  This script is not officially endorsed by Habitica. Use in accordance with [Habitica’s Terms of Service](https://habitica.com/static/terms). The author assumes no responsibility for API changes or account lockouts due to excessive use.

---

**Empower your productivity—automate your Habitica tasksefficiently!**
