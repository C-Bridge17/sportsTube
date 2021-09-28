import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Redirect } from 'react-router-dom';
import { login } from '../../store/session';
import SignUpForm from './SignUpForm';
import './auth.css'

const LoginForm = () => {
  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [demoEmail, setDemoEmail] = useState('demo@aa.io');
  const [demoPassword, setDemoPassword] = useState('password');
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();

  const onLogin = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data) {
      setErrors(data);
    }
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  if (user) {
    return <Redirect to='/' />;
  }

  const demoUser = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(demoEmail, demoPassword));
    if (data) {
      setErrors(data);
    }
  }
  return (
    <div className='auth-page'>
      <h1>SportsTube</h1>
      <div className='login-signup-page'>
        <div className='login-form'>
          <h4>Login</h4>
          <form onSubmit={onLogin}>
            <div>
              {errors.map((error, ind) => (
                <div key={ind}>{error}</div>
              ))}
            </div>
            <div>
              <label htmlFor='email'>Email </label>
              <input
                name='email'
                type='text'
                placeholder='Email'
                value={email}
                onChange={updateEmail}
              />
            </div>
            <div>
              <label htmlFor='password'>Password </label>
              <input
                name='password'
                type='password'
                placeholder='Password'
                value={password}
                onChange={updatePassword}
              />
              <div className='buttons-form'>
                <button type='submit'>Login </button>
                <button type='button' onClick={demoUser}>Demo Login</button>
              </div>
            </div>
          </form>
        </div>
        <div className='signup-form'>

          <h4>Sign Up</h4>
          <SignUpForm />
        </div>
      </div>
    </div>
  );
};

export default LoginForm;
