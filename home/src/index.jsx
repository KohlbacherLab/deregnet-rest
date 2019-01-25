import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter } from 'react-router-dom';
import App from './components/app.jsx';
import 'bootstrap';

import 'bootstrap/dist/css/bootstrap.css';
import './index.css';

ReactDOM.render(
  <BrowserRouter>
		<App />
	</BrowserRouter>,
	document.getElementById('app')
);
