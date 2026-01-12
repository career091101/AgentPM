import React, { useEffect } from 'react';
import { usePosts } from '../contexts/PostsContext';
import useUndoRedo from '../hooks/useUndoRedo';

export default function ManualEditTab() {
  const { state, dispatch } = usePosts();
  const { value, setValue, undo, redo, canUndo, canRedo } = useUndoRedo(
    state.editMode.draftContent
  );

  // AI修正などで draftContent が外部から更新された場合に反映
  useEffect(() => {
    if (state.editMode.draftContent !== value) {
      setValue(state.editMode.draftContent);
    }
  }, [state.editMode.draftContent]);

  const handleChange = (e) => {
    setValue(e.target.value);
    dispatch({ type: 'UPDATE_DRAFT', payload: e.target.value });
  };

  return (
    <div className="space-y-4">
      {/* Undo/Redoボタン */}
      <div className="flex gap-2">
        <button
          onClick={undo}
          disabled={!canUndo}
          className="px-3 py-1 text-sm border rounded disabled:opacity-50 disabled:cursor-not-allowed"
        >
          ← 元に戻す
        </button>
        <button
          onClick={redo}
          disabled={!canRedo}
          className="px-3 py-1 text-sm border rounded disabled:opacity-50 disabled:cursor-not-allowed"
        >
          やり直す →
        </button>
      </div>

      {/* テキストエリア */}
      <textarea
        value={value}
        onChange={handleChange}
        className="w-full h-64 p-4 border rounded-lg resize-none focus:outline-none focus:ring-2 focus:ring-blue-500"
        placeholder="投稿内容を編集..."
      />

      {/* 文字数カウント */}
      <div className="text-sm text-gray-500">
        文字数: {value.length}字
      </div>
    </div>
  );
}
