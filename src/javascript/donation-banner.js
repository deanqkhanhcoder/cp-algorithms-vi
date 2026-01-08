document.addEventListener("DOMContentLoaded", () => {
  const STORAGE_KEY = "donationBannerHiddenUntil";
  const HIDE_DAYS = 30; // 30 ngày hiện lại 1 lần cho đỡ phiền

  const hiddenUntil = Number(localStorage.getItem(STORAGE_KEY) || 0);
  if (Date.now() < hiddenUntil) return;

  const banner = document.createElement("aside");
  banner.id = "donation-banner";
  banner.className = "md-typeset"; // Kế thừa font của MkDocs

  // Thêm icon trái tim và cấu trúc flexbox
  banner.innerHTML = `
    <div class="donation-banner-container">
      <div class="donation-icon">❤️</div>
      <div class="donation-content">
        <p class="donation-text">
          <strong>Bạn thấy bản dịch này có ích?</strong><br>
          Bạn cũng có thể mời tôi <a class="donation-link" href="https://github.com/deanqkhanhcoder/donate" target="_blank">1 ly cafe</a> để tôi có thể tiếp tục cải thiện bản dịch này.
        </p>
      </div>
      <button class="donation-close" type="button" aria-label="Dismiss">
        <svg viewBox="0 0 24 24" width="18" height="18"><path fill="currentColor" d="M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z"/></svg>
      </button>
    </div>
  `;

  // Chèn vào đầu phần nội dung
  const content = document.querySelector(".md-content__inner") || document.querySelector(".md-content") || document.body;

  // Hiệu ứng Fade-in nhẹ
  banner.style.opacity = "0";
  banner.style.transition = "opacity 0.5s ease";
  content.insertBefore(banner, content.firstChild);

  // Trigger animation
  setTimeout(() => banner.style.opacity = "1", 100);

  banner.querySelector(".donation-close").addEventListener("click", () => {
    banner.style.opacity = "0";
    setTimeout(() => {
      banner.remove();
      const until = Date.now() + HIDE_DAYS * 24 * 60 * 60 * 1000;
      localStorage.setItem(STORAGE_KEY, String(until));
    }, 500);
  });
});