import React, { createContext, useReducer, useContext } from 'react';

const initialState = {
  postsData: null,
  selectedPost: null,
  editMode: {
    isOpen: false,
    activeTab: 'manual',
    draftContent: '',
    refineHistory: []
  },
  scheduleMode: {
    isOpen: false,
    scheduledTime: null,
    platforms: ['LinkedIn', 'X', 'Facebook', 'Threads']
  },
  queueMode: {
    isActive: false,      // キューモードのON/OFF
    queueId: null,        // 編集/スケジュール対象のキューID
    variantIndex: null,   // 未承認キューの場合のバリエーションインデックス（0-2）
    isApproved: false,    // 承認済みキューか未承認キューか
    content: null         // 編集対象の投稿内容
  },
  approvalResult: null,
  loading: false,
  error: null
};

function postsReducer(state, action) {
  switch (action.type) {
    case 'LOAD_POSTS':
      return { ...state, postsData: action.payload, loading: false };
    case 'SELECT_POST':
      return { ...state, selectedPost: action.payload };
    case 'OPEN_EDIT_MODAL':
      return {
        ...state,
        editMode: {
          isOpen: true,
          activeTab: 'manual',
          draftContent: action.payload.content,
          refineHistory: []
        }
      };
    case 'CLOSE_EDIT_MODAL':
      return { ...state, editMode: initialState.editMode };
    case 'UPDATE_DRAFT':
      return {
        ...state,
        editMode: { ...state.editMode, draftContent: action.payload }
      };
    case 'APPROVE':
      return { ...state, approvalResult: action.payload };
    case 'OPEN_SCHEDULE_MODAL':
      return {
        ...state,
        scheduleMode: {
          isOpen: true,
          scheduledTime: action.payload.scheduledTime || null,
          platforms: action.payload.platforms || ['LinkedIn', 'X', 'Facebook', 'Threads']
        }
      };
    case 'CLOSE_SCHEDULE_MODAL':
      return { ...state, scheduleMode: initialState.scheduleMode };
    case 'UPDATE_SCHEDULE_TIME':
      return {
        ...state,
        scheduleMode: { ...state.scheduleMode, scheduledTime: action.payload }
      };
    case 'UPDATE_SCHEDULE_PLATFORMS':
      return {
        ...state,
        scheduleMode: { ...state.scheduleMode, platforms: action.payload }
      };
    case 'OPEN_QUEUE_EDIT':
      return {
        ...state,
        queueMode: {
          isActive: true,
          queueId: action.payload.queueId,
          variantIndex: action.payload.variantIndex,
          isApproved: action.payload.isApproved || false,
          content: action.payload.content
        },
        editMode: {
          isOpen: true,
          activeTab: 'manual',
          draftContent: action.payload.content,
          refineHistory: []
        }
      };
    case 'CLOSE_QUEUE_EDIT':
      return {
        ...state,
        queueMode: initialState.queueMode,
        editMode: initialState.editMode
      };
    case 'OPEN_QUEUE_SCHEDULE':
      return {
        ...state,
        queueMode: {
          isActive: true,
          queueId: action.payload.queueId,
          variantIndex: null,
          isApproved: true,
          content: action.payload.content
        },
        scheduleMode: {
          isOpen: true,
          scheduledTime: null,
          platforms: ['X', 'Threads']
        }
      };
    case 'CLOSE_QUEUE_SCHEDULE':
      return {
        ...state,
        queueMode: initialState.queueMode,
        scheduleMode: initialState.scheduleMode
      };
    default:
      return state;
  }
}

const PostsContext = createContext();

export function PostsProvider({ children }) {
  const [state, dispatch] = useReducer(postsReducer, initialState);

  return (
    <PostsContext.Provider value={{ state, dispatch }}>
      {children}
    </PostsContext.Provider>
  );
}

export function usePosts() {
  return useContext(PostsContext);
}
