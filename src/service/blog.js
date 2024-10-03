export const getAllBlog = () => {
    return fetch("https://nathansakkriou.com/api/v1/cap-nord/blogs").then(res => res.json())
}