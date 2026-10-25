import random


# Each question contains:
# id, skill, question, correct answer, wrong answers

def make_question(career, number, skill, question, correct, *wrong):
    return {
        "id": f"{career}_{number:02d}",
        "skill": skill,
        "question": question,
        "correct": correct,
        "options": [correct, *wrong]
    }


QUESTION_BANKS = {

    # =====================================================
    # 1. PYTHON DEVELOPER
    # =====================================================
    "Python Developer": [
        make_question("python", 1, "Programming Basics",
                      "Which keyword defines a function in Python?",
                      "def", "function", "func", "define"),

        make_question("python", 2, "Programming Basics",
                      "Which data type stores True or False?",
                      "bool", "str", "list", "dict"),

        make_question("python", 3, "Programming Basics",
                      "What is the output of len([10, 20, 30])?",
                      "3", "2", "4", "30"),

        make_question("python", 4, "Programming Basics",
                      "Which symbol starts a comment in Python?",
                      "#", "//", "/*", "--"),

        make_question("python", 5, "Programming Basics",
                      "Which collection stores key-value pairs?",
                      "Dictionary", "List", "Tuple", "Set"),

        make_question("python", 6, "Programming Basics",
                      "What does range(3) produce?",
                      "0, 1, 2", "1, 2, 3", "0, 1, 2, 3", "3 only"),

        make_question("python", 7, "Programming Basics",
                      "Which keyword handles an exception?",
                      "except", "error", "catch", "handle"),

        make_question("python", 8, "Programming Basics",
                      "Which keyword creates a class?",
                      "class", "object", "struct", "type"),

        make_question("python", 9, "Programming Basics",
                      "What does append() do to a list?",
                      "Adds an item to the end",
                      "Removes the first item",
                      "Sorts the list",
                      "Deletes the list"),

        make_question("python", 10, "Problem Solving",
                      "Which structure repeats while a condition is true?",
                      "while loop", "if statement", "import statement",
                      "return statement"),

        make_question("python", 11, "Programming Basics",
                      "Which operator checks equality?",
                      "==", "=", "!=", ":="),

        make_question("python", 12, "Programming Basics",
                      "What does int('25') return?",
                      "The integer 25", "The string '25'",
                      "The float 25.5", "An error in every case"),

        make_question("python", 13, "Databases",
                      "Which Python library can connect to SQLite?",
                      "sqlite3", "turtle", "random", "math"),

        make_question("python", 14, "Web Development",
                      "Which Python framework is commonly used to build web apps?",
                      "Flask", "NumPy", "Pillow", "Tkinter"),

        make_question("python", 15, "Programming Basics",
                      "What is a tuple?",
                      "An ordered collection that is immutable",
                      "A function that runs forever",
                      "A database table",
                      "A type of loop"),

        make_question("python", 16, "Problem Solving",
                      "What is recursion?",
                      "A function calling itself",
                      "A loop that cannot stop",
                      "Deleting a variable",
                      "Importing a module"),

        make_question("python", 17, "Programming Basics",
                      "Which keyword exits a loop immediately?",
                      "break", "skip", "stop", "exitloop"),

        make_question("python", 18, "Programming Basics",
                      "What does len('SkillBridge') return?",
                      "11", "10", "12", "SkillBridge"),

        make_question("python", 19, "Programming Basics",
                      "Which statement imports the random module?",
                      "import random", "include random",
                      "using random", "load random"),

        make_question("python", 20, "Problem Solving",
                      "What is the purpose of a unit test?",
                      "To test a small part of a program",
                      "To design a computer",
                      "To replace the database",
                      "To install an operating system"),
    ],


    # =====================================================
    # 2. FRONTEND DEVELOPER
    # =====================================================
    "Frontend Developer": [
        make_question("frontend", 1, "Web Development",
                      "What does HTML define?",
                      "Webpage structure", "Database tables",
                      "Server hardware", "Network routing"),

        make_question("frontend", 2, "Web Development",
                      "What is CSS primarily used for?",
                      "Styling webpages", "Managing databases",
                      "Sending emails", "Compiling Java"),

        make_question("frontend", 3, "Web Development",
                      "Which HTML element creates a hyperlink?",
                      "<a>", "<linkto>", "<href>", "<url>"),

        make_question("frontend", 4, "Web Development",
                      "Which CSS property changes text colour?",
                      "color", "font-style", "background-image", "display"),

        make_question("frontend", 5, "Web Development",
                      "Which JavaScript keyword declares a block-scoped variable?",
                      "let", "define", "dim", "declare"),

        make_question("frontend", 6, "Web Development",
                      "Which method selects an element by its ID?",
                      "document.getElementById()",
                      "document.getClass()",
                      "window.getID()",
                      "document.selectName()"),

        make_question("frontend", 7, "Web Development",
                      "What does responsive design mean?",
                      "Layouts adapt to different screen sizes",
                      "Pages only work on desktops",
                      "Images never change size",
                      "Websites do not use CSS"),

        make_question("frontend", 8, "Web Development",
                      "Which CSS layout system is one-dimensional?",
                      "Flexbox", "Grid", "SQL", "DOM"),

        make_question("frontend", 9, "Web Development",
                      "Which HTML attribute provides alternative image text?",
                      "alt", "titleonly", "srcsetonly", "caption"),

        make_question("frontend", 10, "Web Development",
                      "Which event occurs when a user clicks an element?",
                      "click", "hoveredonly", "submitonly", "loadcss"),

        make_question("frontend", 11, "Web Development",
                      "Which method converts JSON text into a JavaScript value?",
                      "JSON.parse()", "JSON.stringify()",
                      "JSON.convert()", "JSON.read()"),

        make_question("frontend", 12, "Web Development",
                      "Which CSS rule adds space inside an element's border?",
                      "padding", "margin", "outline", "gap-only"),

        make_question("frontend", 13, "Web Development",
                      "What is the DOM?",
                      "A representation of a webpage as objects",
                      "A database server",
                      "A CSS framework",
                      "A network protocol"),

        make_question("frontend", 14, "Web Development",
                      "Which HTML element is used for a form?",
                      "<form>", "<inputform>", "<fieldsetpage>", "<submit>"),

        make_question("frontend", 15, "Web Development",
                      "Which CSS feature helps create two-dimensional layouts?",
                      "CSS Grid", "Float only", "HTML tables only",
                      "JavaScript alerts"),

        make_question("frontend", 16, "Web Development",
                      "What does fetch() commonly do in JavaScript?",
                      "Makes network requests",
                      "Changes a CSS file automatically",
                      "Creates a database table",
                      "Compiles HTML"),

        make_question("frontend", 17, "Web Development",
                      "Which HTML element represents the main page content?",
                      "<main>", "<footer>", "<aside>", "<meta>"),

        make_question("frontend", 18, "Web Development",
                      "What does the CSS media query help with?",
                      "Applying styles based on device conditions",
                      "Creating database queries",
                      "Encrypting passwords",
                      "Running Python code"),

        make_question("frontend", 19, "Web Development",
                      "Which JavaScript method adds an item to an array's end?",
                      "push()", "pop()", "shift()", "slice()"),

        make_question("frontend", 20, "Problem Solving",
                      "What should you inspect when a button does not work?",
                      "The event handler and browser console",
                      "Only the monitor brightness",
                      "The computer wallpaper",
                      "The keyboard language"),
    ],


    # =====================================================
    # 3. JAVA DEVELOPER
    # =====================================================
    "Java Developer": [
        make_question("java", 1, "Programming Basics",
                      "Which method is the usual entry point of a Java application?",
                      "main()", "startApp()", "runJava()", "begin()"),

        make_question("java", 2, "Programming Basics",
                      "Which keyword creates an object?",
                      "new", "make", "create", "object"),

        make_question("java", 3, "Programming Basics",
                      "Which keyword declares a class?",
                      "class", "struct", "define", "moduleclass"),

        make_question("java", 4, "Programming Basics",
                      "Which type stores a true or false value?",
                      "boolean", "String", "char", "double"),

        make_question("java", 5, "Programming Basics",
                      "What is inheritance in Java?",
                      "A class acquiring features from another class",
                      "Deleting an object",
                      "Converting Java into HTML",
                      "Storing files in a folder"),

        make_question("java", 6, "Programming Basics",
                      "Which keyword prevents a method from being overridden?",
                      "final", "static", "void", "public"),

        make_question("java", 7, "Programming Basics",
                      "Which collection commonly stores key-value pairs?",
                      "HashMap", "ArrayList", "HashSet", "Stack"),

        make_question("java", 8, "Programming Basics",
                      "Which block is commonly used to handle exceptions?",
                      "catch", "repeat", "check", "rescue"),

        make_question("java", 9, "Programming Basics",
                      "What is method overloading?",
                      "Methods with the same name but different parameter lists",
                      "Deleting methods",
                      "Using multiple packages",
                      "Running one method forever"),

        make_question("java", 10, "Programming Basics",
                      "Which keyword refers to the current object?",
                      "this", "self", "current", "object"),

        make_question("java", 11, "Programming Basics",
                      "Which type is used for whole numbers such as 42?",
                      "int", "boolean", "char", "String"),

        make_question("java", 12, "Programming Basics",
                      "Which access modifier allows access from anywhere?",
                      "public", "private", "protected-only", "hidden"),

        make_question("java", 13, "Programming Basics",
                      "What is an interface used for?",
                      "Defining a contract of methods and constants",
                      "Storing only images",
                      "Replacing every class",
                      "Creating HTML pages"),

        make_question("java", 14, "Databases",
                      "Which Java API is commonly used for database access?",
                      "JDBC", "JDK-UI", "JImage", "JCSS"),

        make_question("java", 15, "Problem Solving",
                      "Which loop checks its condition before each iteration?",
                      "while", "do-while only after the body",
                      "switch", "try"),

        make_question("java", 16, "Programming Basics",
                      "Which keyword is used to implement an interface?",
                      "implements", "inherits", "extends-interface",
                      "instance"),

        make_question("java", 17, "Programming Basics",
                      "What is encapsulation?",
                      "Bundling data and methods while controlling access",
                      "Copying all files",
                      "Deleting class variables",
                      "Running several loops"),

        make_question("java", 18, "Programming Basics",
                      "Which type is used for text strings?",
                      "String", "Text", "char[] only", "Word"),

        make_question("java", 19, "Problem Solving",
                      "What does debugging help developers do?",
                      "Find and fix program defects",
                      "Increase screen resolution",
                      "Replace source code with images",
                      "Create a network cable"),

        make_question("java", 20, "Programming Basics",
                      "Which keyword returns a value from a method?",
                      "return", "send", "yieldvalue", "output"),
    ],


    # =====================================================
    # 4. FULL STACK DEVELOPER
    # =====================================================
    "Full Stack Developer": [
        make_question("fullstack", 1, "Web Development",
                      "What does HTML provide in a web application?",
                      "Page structure", "Database indexing",
                      "Password hashing", "Network routing"),

        make_question("fullstack", 2, "Web Development",
                      "What is CSS used for?",
                      "Styling the user interface",
                      "Executing SQL queries",
                      "Managing server memory",
                      "Encrypting database backups"),

        make_question("fullstack", 3, "Web Development",
                      "What is JavaScript commonly used for in the browser?",
                      "Adding interactivity", "Creating physical hardware",
                      "Replacing the operating system", "Routing network cables"),

        make_question("fullstack", 4, "Web Development",
                      "What does an HTTP GET request normally do?",
                      "Requests a resource", "Deletes a database",
                      "Creates a password", "Restarts a server"),

        make_question("fullstack", 5, "Web Development",
                      "What is an API?",
                      "An interface that lets software systems communicate",
                      "A CSS colour",
                      "A physical storage device",
                      "A programming error"),

        make_question("fullstack", 6, "Databases",
                      "Which SQL command retrieves records?",
                      "SELECT", "REMOVE", "FETCHFILE", "DISPLAYALL"),

        make_question("fullstack", 7, "Databases",
                      "What is a primary key?",
                      "A field that uniquely identifies a row",
                      "A password for every website",
                      "A CSS selector",
                      "A backup folder"),

        make_question("fullstack", 8, "Web Development",
                      "What does a server-side framework help developers build?",
                      "Backend web functionality",
                      "Computer monitors",
                      "Keyboard drivers only",
                      "Image file formats"),

        make_question("fullstack", 9, "Programming Basics",
                      "What is version control used for?",
                      "Tracking and managing code changes",
                      "Changing screen brightness",
                      "Compressing every image",
                      "Replacing all tests"),

        make_question("fullstack", 10, "Databases",
                      "Why should database queries use parameterized inputs?",
                      "To reduce SQL injection risk",
                      "To make passwords visible",
                      "To disable validation",
                      "To remove database tables"),

        make_question("fullstack", 11, "Web Development",
                      "What does responsive design help achieve?",
                      "Usable layouts across screen sizes",
                      "Faster typing on every keyboard",
                      "Automatic database backups",
                      "Unlimited server storage"),

        make_question("fullstack", 12, "Networking",
                      "What does DNS do?",
                      "Resolves domain names to network addresses",
                      "Styles web pages",
                      "Stores SQL rows",
                      "Compiles JavaScript"),

        make_question("fullstack", 13, "Web Development",
                      "What is JSON commonly used for?",
                      "Exchanging structured data",
                      "Styling buttons",
                      "Encrypting every connection",
                      "Creating hardware drivers"),

        make_question("fullstack", 14, "Programming Basics",
                      "Why is input validation important?",
                      "To check data before processing it",
                      "To hide every form field",
                      "To skip error handling",
                      "To remove authentication"),

        make_question("fullstack", 15, "Databases",
                      "What is a database transaction?",
                      "A group of operations treated as a unit",
                      "A CSS animation",
                      "A browser bookmark",
                      "A network cable"),

        make_question("fullstack", 16, "Web Development",
                      "What does HTTP status code 404 generally mean?",
                      "The requested resource was not found",
                      "The request succeeded",
                      "The server restarted successfully",
                      "The user is always authenticated"),

        make_question("fullstack", 17, "Networking",
                      "What does HTTPS add to HTTP?",
                      "TLS-based connection security",
                      "Automatic CSS generation",
                      "A database schema",
                      "A programming language"),

        make_question("fullstack", 18, "Programming Basics",
                      "What is a unit test?",
                      "A test of a small unit of code",
                      "A test of monitor hardware",
                      "A database migration only",
                      "A website logo"),

        make_question("fullstack", 19, "Web Development",
                      "What does a frontend form usually send to a backend?",
                      "User-entered data",
                      "The computer's wallpaper",
                      "The monitor serial number",
                      "Only CSS colours"),

        make_question("fullstack", 20, "Problem Solving",
                      "What is a useful first step when a web request fails?",
                      "Inspect the error message and request details",
                      "Delete the entire project",
                      "Ignore the browser console",
                      "Remove all server logs"),
    ],


    # =====================================================
    # 5. CYBERSECURITY ANALYST
    # =====================================================
    "Cybersecurity Analyst": [
        make_question("cyber", 1, "Networking",
                      "What is the purpose of a firewall?",
                      "To control network traffic according to rules",
                      "To style a website",
                      "To store spreadsheet formulas",
                      "To increase monitor brightness"),

        make_question("cyber", 2, "Networking",
                      "What does HTTPS help protect?",
                      "Data exchanged over a connection using TLS",
                      "A computer from every possible attack",
                      "Files from all hardware failures",
                      "A website's colour scheme"),

        make_question("cyber", 3, "Programming Basics",
                      "What is phishing?",
                      "A deceptive attempt to obtain sensitive information",
                      "A method of compressing files",
                      "A database indexing technique",
                      "A network speed test"),

        make_question("cyber", 4, "Programming Basics",
                      "Why should passwords be stored as secure hashes?",
                      "To avoid storing plaintext passwords",
                      "To make passwords public",
                      "To make every password identical",
                      "To disable user accounts"),

        make_question("cyber", 5, "Networking",
                      "What does an IP address identify?",
                      "A network interface's address",
                      "A person's password",
                      "A file's programming language",
                      "A keyboard shortcut"),

        make_question("cyber", 6, "Networking",
                      "What does DNS do?",
                      "Resolves domain names to network addresses",
                      "Hashes passwords",
                      "Creates database backups",
                      "Checks HTML accessibility"),

        make_question("cyber", 7, "Problem Solving",
                      "What is a vulnerability?",
                      "A weakness that could be exploited",
                      "A confirmed backup",
                      "A software update",
                      "A secure password policy"),

        make_question("cyber", 8, "Programming Basics",
                      "What is multi-factor authentication?",
                      "Using multiple types of evidence to verify identity",
                      "Using the same password twice",
                      "Disabling login checks",
                      "Sharing one account with everyone"),

        make_question("cyber", 9, "Networking",
                      "What is the purpose of a VPN?",
                      "To create a protected network connection",
                      "To replace every password",
                      "To remove all malware automatically",
                      "To increase CPU memory"),

        make_question("cyber", 10, "Problem Solving",
                      "What should an analyst do when investigating an incident?",
                      "Preserve evidence and follow the response process",
                      "Delete all logs immediately",
                      "Share credentials publicly",
                      "Ignore suspicious activity"),

        make_question("cyber", 11, "Programming Basics",
                      "What is the principle of least privilege?",
                      "Grant only the access needed for a task",
                      "Give every user administrator access",
                      "Disable all authentication",
                      "Use one account for everyone"),

        make_question("cyber", 12, "Networking",
                      "What does a network port help identify?",
                      "A service or application endpoint",
                      "A monitor's physical size",
                      "A user's real name",
                      "A password's length only"),

        make_question("cyber", 13, "Programming Basics",
                      "What is encryption used for?",
                      "Protecting information by transforming it with a key",
                      "Deleting all data",
                      "Making data publicly readable",
                      "Replacing network protocols"),

        make_question("cyber", 14, "Problem Solving",
                      "What is a security log useful for?",
                      "Investigating events and suspicious activity",
                      "Changing a webpage's font",
                      "Increasing disk capacity",
                      "Replacing authentication"),

        make_question("cyber", 15, "Networking",
                      "What is the role of an intrusion detection system?",
                      "Identifying suspicious activity or policy violations",
                      "Designing webpage layouts",
                      "Writing database records only",
                      "Replacing all backups"),

        make_question("cyber", 16, "Programming Basics",
                      "Why are software updates important?",
                      "They can fix security vulnerabilities and bugs",
                      "They always remove the need for passwords",
                      "They make backups unnecessary",
                      "They disable all network connections"),

        make_question("cyber", 17, "Networking",
                      "Which protocol is commonly used for secure remote shell access?",
                      "SSH", "FTP", "Telnet", "HTTP"),

        make_question("cyber", 18, "Problem Solving",
                      "What is a false positive in security monitoring?",
                      "A benign event incorrectly flagged as suspicious",
                      "A real attack that was confirmed",
                      "A successful backup",
                      "A patched vulnerability"),

        make_question("cyber", 19, "Databases",
                      "What is a benefit of restricting database permissions?",
                      "It limits unauthorized access and changes",
                      "It makes every table public",
                      "It disables audit logging",
                      "It exposes credentials"),

        make_question("cyber", 20, "Problem Solving",
                      "What is a good response to a suspicious email?",
                      "Verify it through a trusted channel and report it",
                      "Open every attachment",
                      "Send your password to the sender",
                      "Forward it to all contacts"),
    ],


    # =====================================================
    # 6. DATA ANALYST
    # =====================================================
    "Data Analyst": [
        make_question("data", 1, "Databases",
                      "Which SQL command retrieves data?",
                      "SELECT", "DELETE", "DROP", "ALTER"),

        make_question("data", 2, "Databases",
                      "Which SQL function calculates the average?",
                      "AVG()", "COUNT()", "SUMONLY()", "MEANROW()"),

        make_question("data", 3, "Databases",
                      "What does GROUP BY do in SQL?",
                      "Groups rows for aggregate calculations",
                      "Deletes duplicate tables automatically",
                      "Changes column names",
                      "Encrypts database files"),

        make_question("data", 4, "Programming Basics",
                      "Which Python library is commonly used for tabular data analysis?",
                      "pandas", "turtle", "pygame", "tkinter"),

        make_question("data", 5, "Programming Basics",
                      "What is a DataFrame in pandas?",
                      "A two-dimensional labelled data structure",
                      "A network router",
                      "A CSS layout",
                      "A password hashing algorithm"),

        make_question("data", 6, "Problem Solving",
                      "What is the median?",
                      "The middle value in ordered data",
                      "Always the largest value",
                      "Always the most frequent value",
                      "The sum of all values"),

        make_question("data", 7, "Problem Solving",
                      "What is the mean of 2, 4, and 6?",
                      "4", "3", "6", "12"),

        make_question("data", 8, "Databases",
                      "What does a SQL JOIN do?",
                      "Combines related rows from tables",
                      "Deletes every table",
                      "Creates a chart automatically",
                      "Changes a database password"),

        make_question("data", 9, "Problem Solving",
                      "What is an outlier?",
                      "A value unusually distant from other observations",
                      "Always the average",
                      "A missing column name",
                      "A type of database key"),

        make_question("data", 10, "Problem Solving",
                      "What is data cleaning?",
                      "Correcting or handling inaccurate, inconsistent, or missing data",
                      "Deleting every row",
                      "Changing all numbers to zero",
                      "Creating a computer network"),

        make_question("data", 11, "Databases",
                      "Which SQL clause filters rows before grouping?",
                      "WHERE", "ORDER BY", "SELECT", "CREATE"),

        make_question("data", 12, "Databases",
                      "Which SQL clause filters grouped results?",
                      "HAVING", "VALUES", "INSERT", "UPDATE"),

        make_question("data", 13, "Problem Solving",
                      "What does correlation measure?",
                      "The strength and direction of association",
                      "Proof that one variable causes another",
                      "The number of database tables",
                      "A file's size"),

        make_question("data", 14, "Problem Solving",
                      "What is a histogram useful for?",
                      "Showing the distribution of numerical values",
                      "Showing website navigation links",
                      "Encrypting records",
                      "Managing user permissions"),

        make_question("data", 15, "Programming Basics",
                      "What does a missing value represent in a dataset?",
                      "An unavailable or unrecorded value",
                      "Always the number zero",
                      "Always a duplicate row",
                      "A database primary key"),

        make_question("data", 16, "Databases",
                      "What is a primary key?",
                      "A field that uniquely identifies a row",
                      "A chart title",
                      "A statistical average",
                      "A missing data marker"),

        make_question("data", 17, "Problem Solving",
                      "Why should data be visualized?",
                      "To communicate patterns and trends clearly",
                      "To guarantee that data is correct",
                      "To eliminate the need for analysis",
                      "To encrypt every spreadsheet"),

        make_question("data", 18, "Programming Basics",
                      "Which Python expression creates a list?",
                      "[1, 2, 3]", "{1: 2}", "(1)", "range{'1,2,3'}"),

        make_question("data", 19, "Problem Solving",
                      "What is a sample in statistics?",
                      "A subset of a population",
                      "The entire population in every case",
                      "A chart legend",
                      "A database password"),

        make_question("data", 20, "Problem Solving",
                      "Why should analysts validate their results?",
                      "To check accuracy and identify possible errors",
                      "To guarantee every hypothesis is true",
                      "To remove all uncertainty",
                      "To avoid documenting assumptions"),
    ],
}



def get_random_questions(career, count=10):
    """
    Select questions as evenly as possible across available skill categories.
    Shuffle the question order and answer options.
    """

    bank = QUESTION_BANKS.get(career)

    if not bank:
        return []

    # Group questions by skill category.
    questions_by_skill = {}

    for question in bank:
        skill = question["skill"]

        if skill not in questions_by_skill:
            questions_by_skill[skill] = []

        questions_by_skill[skill].append(question)

    # Shuffle questions within each category.
    skills = list(questions_by_skill.keys())

    for skill in skills:
        random.shuffle(questions_by_skill[skill])

    # Shuffle skill order for variety.
    random.shuffle(skills)

    # Select questions evenly across categories.
    selected = []
    target_count = min(count, len(bank))

    while len(selected) < target_count:
        added_question = False

        for skill in skills:
            if questions_by_skill[skill] and len(selected) < target_count:
                selected.append(questions_by_skill[skill].pop())
                added_question = True

        if not added_question:
            break

    # Shuffle the order in which questions are displayed.
    random.shuffle(selected)

    # Copy each question and shuffle its answer options.
    questions = []

    for original in selected:
        question = {
            "id": original["id"],
            "skill": original["skill"],
            "question": original["question"],
            "correct": original["correct"],
            "options": original["options"].copy()
        }

        random.shuffle(question["options"])
        questions.append(question)

    return questions
