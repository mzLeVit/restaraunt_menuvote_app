import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import axios from 'axios';

const MenuPage: React.FC = () => {
  const dispatch = useDispatch();
  const menu = useSelector((state: any) => state.menu);

  useEffect(() => {
    axios.get('/api/v1/menu/today').then((response) => {
      dispatch({ type: 'SET_MENU', payload: response.data });
    });
  }, [dispatch]);

  return (
    <div>
      <h1>Today's Menu</h1>
      <ul>
        {menu.map((item: any) => (
          <li key={item.id}>{item.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default MenuPage;
