import React from 'react';
import { render, fireEvent } from '@testing-library/react-native';
import LoginScreen from '../LoginScreen';

test('renders login screen inputs and buttons', () => {
  const { getByPlaceholderText, getByText } = render(<LoginScreen />);
  expect(getByPlaceholderText('Email')).toBeTruthy();
  expect(getByPlaceholderText('Password')).toBeTruthy();
  expect(getByText('Login')).toBeTruthy();
  expect(getByText('Register')).toBeTruthy();
});