import { createStore } from 'redux';


const initialState = { menu: [], user: null };

function reducer(state = initialState, action: any) {
  switch (action.type) {
    case 'SET_MENU':
      return { ...state, menu: action.payload };
    case 'SET_USER':
      return { ...state, user: action.payload };
    default:
      return state;
  }
}

export const store = createStore(reducer);
