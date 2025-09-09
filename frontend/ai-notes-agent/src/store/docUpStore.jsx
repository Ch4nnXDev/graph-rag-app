import { create } from "zustand";

export const uiStore = create((set)=> ({
    window: 'chat',
    setWindow: (name) => set({ window: name }),
}));