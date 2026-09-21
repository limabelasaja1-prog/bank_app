* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    padding: 20px;
}

.container {
    max-width: 1000px;
    margin: 0 auto;
    background: white;
    border-radius: 10px;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
    overflow: hidden;
}

header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 30px 20px;
    text-align: center;
}

header h1 {
    font-size: 2.5em;
    margin-bottom: 10px;
}

header p {
    font-size: 1.1em;
    opacity: 0.9;
}

.form-section {
    padding: 30px 20px;
    background: #f8f9fa;
    border-bottom: 1px solid #e9ecef;
}

.form-section h2 {
    color: #333;
    margin-bottom: 20px;
    font-size: 1.5em;
}

.form-group {
    margin-bottom: 15px;
}

label {
    display: block;
    margin-bottom: 8px;
    color: #333;
    font-weight: 500;
}

input[type="text"],
select,
textarea {
    width: 100%;
    padding: 12px;
    border: 1px solid #ddd;
    border-radius: 5px;
    font-size: 1em;
    transition: border-color 0.3s;
}

input[type="text"]:focus,
select:focus,
textarea:focus {
    outline: none;
    border-color: #667eea;
    box-shadow: 0 0 5px rgba(102, 126, 234, 0.3);
}

textarea {
    resize: vertical;
    font-family: inherit;
}

.btn {
    padding: 12px 30px;
    border: none;
    border-radius: 5px;
    font-size: 1em;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s;
}

.btn-primary {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
}

.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
}

.btn-edit {
    background: #28a745;
    color: white;
    padding: 8px 15px;
    font-size: 0.9em;
    margin-right: 5px;
}

.btn-edit:hover {
    background: #218838;
}

.btn-delete {
    background: #dc3545;
    color: white;
    padding: 8px 15px;
    font-size: 0.9em;
}

.btn-delete:hover {
    background: #c82333;
}

.table-section {
    padding: 30px 20px;
}

.table-section h2 {
    color: #333;
    margin-bottom: 20px;
    font-size: 1.5em;
}

.message-box {
    margin-bottom: 20px;
    padding: 15px;
    border-radius: 5px;
    display: none;
}

.message-box.success {
    background: #d4edda;
    color: #155724;
    border: 1px solid #c3e6cb;
    display: block;
}

.message-box.error {
    background: #f8d7da;
    color: #721c24;
    border: 1px solid #f5c6cb;
    display: block;
}

.table-wrapper {
    overflow-x: auto;
}

table {
    width: 100%;
    border-collapse: collapse;
}

thead {
    background: #f8f9fa;
}

th {
    padding: 15px;
    text-align: left;
    color: #333;
    font-weight: 600;
    border-bottom: 2px solid #dee2e6;
}

td {
    padding: 15px;
    border-bottom: 1px solid #dee2e6;
}

tbody tr:hover {
    background: #f8f9fa;
}

.empty-state {
    text-align: center;
    color: #999;
}

.badge {
    display: inline-block;
    padding: 6px 12px;
    border-radius: 20px;
    font-size: 0.85em;
    font-weight: 600;
}

.badge-success {
    background: #d4edda;
    color: #155724;
    border: 1px solid #c3e6cb;
}

.badge-danger {
    background: #f8d7da;
    color: #721c24;
    border: 1px solid #f5c6cb;
}

.modal {
    display: none;
    position: fixed;
    z-index: 1;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
}

.modal-content {
    background-color: white;
    margin: 5% auto;
    padding: 30px;
    border-radius: 10px;
    width: 90%;
    max-width: 500px;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
}

.close {
    color: #aaa;
    float: right;
    font-size: 28px;
    font-weight: bold;
    cursor: pointer;
}

.close:hover {
    color: black;
}

.modal-content h2 {
    margin-bottom: 20px;
    color: #333;
}

@media (max-width: 768px) {
    header h1 {
        font-size: 1.8em;
    }

    .form-section,
    .table-section {
        padding: 20px 15px;
    }

    th, td {
        padding: 10px;
        font-size: 0.9em;
    }

    .btn {
        padding: 10px 20px;
        font-size: 0.9em;
    }

    .modal-content {
        width: 95%;
    }
}