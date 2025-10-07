***

# Data Science Interview MCQ App

A **Streamlit-based interactive quiz application** featuring a comprehensive collection of data science multiple-choice questions (MCQs) to help you practice and evaluate your knowledge for interviews, exams, and upskilling.[1]

***

### Features

- **Topic-wise Quizzes**: Contains categorized quizzes covering key Data Science concepts:
  - Statistics, Visualization, Python basics, NumPy, Pandas, EDA, Normal Distribution, Hypothesis Testing, Linear Regression, SVM, Decision Trees, Classification metrics, NLP, Clustering, Recommendation Systems, and more.[1]
- **Rich Explanations**: Each question provides detailed explanations and real-world applications after submission.
- **Performance Feedback**: Get immediate feedback and scoring, including personalized messages (excellent/good/review needed) based on your quiz performance.
- **Session State**: Keeps track of answers between questions and quizzes for a seamless user experience.
- **Retry & Navigation Buttons**: Option to retry quizzes or choose new topics for continuous practice.
- **Clean UI**: Modern styling with feedback colors (green/red) and expandable answer explanations, enhancing clarity and learning.[1]

***

### Demo

1. **Topic Selection**: Choose your preferred topic from the sidebar.
2. **Question Form**: Answer MCQs one at a time in a well-organized form.
3. **Submit & Results**: Upon submission, answers are color-coded. Correct answers show in green, incorrect in red, and explanations are instantly available in expandable sections.
4. **Performance Summary**: See your overall score, percentage, and performance message.
5. **Try Again/Change Topic**: Use simple buttons to retake quizzes or pick another topic.

<img width="1912" height="932" alt="image" src="https://github.com/user-attachments/assets/ceccbf88-dac3-4b1b-b6b9-8862c098aa52" />

<img width="1912" height="932" alt="image" src="https://github.com/user-attachments/assets/6148db83-7a04-4c9f-b542-0380c4966c68" />

<img width="1902" height="7578" alt="image" src="https://github.com/user-attachments/assets/221e7034-b575-4598-9c28-94d1c9925c1e" />

***

### How to Run

#### Requirements

- Python 3.7 or above
- Required packages: `streamlit`, `pandas`, `numpy`, `altair`, and others (install via requirements or notebook cells).[1]

#### Steps

1. **Install Dependencies**:  
   ```bash
   pip install streamlit pandas numpy altair
   ```
2. **Export App Code**: The notebook contains a cell to write the quiz app code to `quizapp.py`.
3. **Launch the App**:  
   ```bash
   streamlit run quizapp.py
   ```
4. **(Optional) Public Link via ngrok**:  
   The notebook demonstrates using `pyngrok` to make the Streamlit app accessible via a public URL, ideal for sharing with peers or interviewees.

***

### Adding / Customizing Questions

- Questions are structured as a list of dictionaries, grouped by topic.
- To add or edit content, modify the `QUIZ_DATA` structure in the main app code and restart the app to reflect your changes.

***

### Interactivity & Architecture

- **Streamlit Forms**: Ensures all questions are answered before submission.
- **Stateful Experience**: Uses `st.session_state` for user answers, submission status, and quiz navigation.
- **Styling**: Custom CSS for clear feedback, visual distinction of correct/incorrect answers, score boxes, and more.[1]

***

### Contribution & Extensions

- Contributions are welcome! You can add new topics, enrich explanations, or propose UI enhancements.
- Ideas for further extensions:
  - Add timed quizzes.
  - Enable detailed per-topic performance tracking.
  - Integrate learning resources based on incorrect answers.

***

### License

Distributed for non-commercial, educational use. Please credit the original author if using this structure in your projects.

***
