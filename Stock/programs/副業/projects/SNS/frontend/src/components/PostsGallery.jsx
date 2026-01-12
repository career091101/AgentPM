import React, { useEffect } from 'react';
import { usePosts } from '../contexts/PostsContext';
import PostCard from './PostCard';
import { getPosts, approvePost } from '../utils/api';
import toast from 'react-hot-toast';

export default function PostsGallery() {
  const { state, dispatch } = usePosts();

  useEffect(() => {
    const fetchPosts = async () => {
      try {
        const data = await getPosts();
        dispatch({ type: 'LOAD_POSTS', payload: data });
      } catch (error) {
        toast.error('投稿案の読み込みに失敗しました');
      }
    };

    fetchPosts();
  }, [dispatch]);

  const handleSelect = async (post, index) => {
    const postWithNum = { ...post, variantNum: `案${index + 1}` };
    dispatch({ type: 'SELECT_POST', payload: postWithNum });

    try {
      await approvePost({
        variant: post.variant,
        content: post.content,
        refined: false,
        refined_content: null
      });
      toast.success(`${post.variant}を選択しました`);
    } catch (error) {
      toast.error('選択の保存に失敗しました');
    }
  };

  const handleEdit = (post, index) => {
    const postWithNum = { ...post, variantNum: `案${index + 1}` };
    dispatch({ type: 'SELECT_POST', payload: postWithNum });
    dispatch({ type: 'OPEN_EDIT_MODAL', payload: { content: post.content } });
  };

  const handleSchedule = async (post, index) => {
    // まず承認を実行
    try {
      await approvePost({
        variant: post.variant,
        content: post.content,
        refined: false,
        refined_content: null
      });

      // スケジューリングモーダルを開く
      dispatch({
        type: 'OPEN_SCHEDULE_MODAL',
        payload: {
          scheduledTime: null,
          platforms: ['LinkedIn', 'X', 'Facebook', 'Threads']
        }
      });

      toast.success(`${post.variant}を承認しました。スケジューリング設定を続けてください。`);
    } catch (error) {
      toast.error('承認に失敗しました');
    }
  };

  if (!state.postsData) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="text-gray-500">投稿案を読み込み中...</div>
      </div>
    );
  }

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      {state.postsData.posts.map((post, index) => (
        <PostCard
          key={index}
          post={post}
          index={index}
          onSelect={() => handleSelect(post, index)}
          onEdit={() => handleEdit(post, index)}
          onSchedule={() => handleSchedule(post, index)}
        />
      ))}
    </div>
  );
}
