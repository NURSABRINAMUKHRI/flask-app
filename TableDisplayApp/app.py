from flask import Flask, render_template
import csv

app = Flask(__name__)

def read_csv(file_path):
    table_data = {}
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            table_data[row[0]] = int(row[1])  # Store data in a dictionary with 'Index #' as key
    return table_data

@app.route('/')
def display_tables():
    # Read CSV data
    table1 = read_csv('Table_Input.csv')
    
    # Process Table 2
    alpha = table1['A5'] + table1['A20']
    beta = table1['A15'] // table1['A7']  # Integer division
    charlie = table1['A13'] * table1['A12']
    
    table2 = {
        'Alpha': alpha,
        'Beta': beta,
        'Charlie': charlie,
    }

    return render_template('index.html', table1=table1, table2=table2)

if __name__ == "__main__":
    app.run(debug=True)
