# Shopify Reviews Section - Installation Guide

## 📁 File Created

`reviews-masonry.liquid` - Shopify custom section with masonry grid layout

---

## 🚀 Installation Steps

### 1. Upload to Shopify

**Option A: Using Theme Editor (Recommended)**

1. Go to **Shopify Admin** → **Online Store** → **Themes**
2. Click **Actions** → **Edit code**
3. In the **Sections** folder, click **Add a new section**
4. Name it: `reviews-masonry`
5. Copy and paste the entire contents of `reviews-masonry.liquid`
6. Click **Save**

**Option B: Using Shopify CLI**

```bash
# Upload to your theme
shopify theme push
```

### 2. Add to Your Homepage

1. Go to **Online Store** → **Themes** → **Customize**
2. Navigate to your **Home page**
3. Click **Add section**
4. Search for **"Reviews Masonry"**
5. Click to add it to your page
6. Position it where you want (recommended: after hero/banner section)

### 3. Customize in Theme Editor

The section comes pre-loaded with **6 real customer reviews**. You can:

**Edit Section Settings:**

- ✏️ Heading text
- ✏️ Subheading text
- 🎨 All colors (background, text, cards, accent)
- 📏 Padding and spacing
- 🔤 Font sizes

**Edit Individual Reviews:**

- Click on any review card
- Modify the review text
- Change reviewer name and initials
- Update follower count
- Adjust star rating (1-5)
- Add/remove Instagram icon

**Add More Reviews:**

- Click **Add block** → **Review**
- Fill in the details
- Repeat for as many reviews as you want

---

## ✨ Features Included

### Fully Customizable

- ✅ **Colors**: 9 color settings (background, text, stars, accent, etc.)
- ✅ **Typography**: Adjustable heading and subheading sizes
- ✅ **Layout**: Container width, padding, border radius
- ✅ **Content**: Unlimited review blocks

### Pre-loaded Reviews

The section comes with **6 real testimonials**:

1. Mariah Tapia (126K followers - Interior Designer)
2. Popham Design (115K followers - Home Decor)
3. Boxwood & Spruce (53K followers - Content Creator)
4. Brooke | Amelia Design (Interior Designer)
5. Mallori Hanes (29K followers - Home Restoration)
6. Happy Customer (9K followers - Design Enthusiast)

### Responsive Design

- 📱 **Mobile**: 1 column
- 📱 **Tablet**: 2 columns
- 💻 **Desktop**: 3 columns (masonry layout)

### Interactive Effects

- Hover animations (lift + shadow)
- Border color change on hover
- Smooth transitions

---

## 🎨 Customization Examples

### Change Color Scheme

**Dark Mode:**

- Background: `#1a2332`
- Heading: `#ffffff`
- Card Background: `#2c3e50`
- Text: `#e5e7eb`

**Brand Colors:**

- Accent Color: Your brand color
- Stars: Gold `#F59E0B` (default)
- Avatar: Match your accent color

### Adjust Layout

- **Wider**: Increase container width to 1600px
- **Tighter**: Decrease padding to 40px top/bottom
- **Rounder cards**: Increase border radius to 16-20px

---

## 📝 Adding Your Own Reviews

### Template for Each Review:

```
Review Text: [Customer testimonial quote]
Avatar Initials: [2-3 letters]
Reviewer Name: [Full name]
Follower Count: [Optional: "50K" or leave blank]
Reviewer Title: [Interior Designer, Homeowner, etc.]
Star Rating: 5
Show Instagram Icon: ✓ (if they have followers)
```

### Best Practices:

- Keep reviews 50-200 characters for visual balance
- Mix long and short reviews for masonry effect
- Include follower counts for influencers
- Use real testimonials for authenticity
- Update regularly with new reviews

---

## 🔧 Troubleshooting

**Section not showing up?**

- Make sure you saved the file in the **Sections** folder
- Refresh the theme customizer
- Check that the file is named `reviews-masonry.liquid`

**Colors not changing?**

- Clear your browser cache
- Save changes in theme customizer
- Check color picker is set correctly

**Reviews overlapping on mobile?**

- This is normal for masonry layout
- Cards will stack in 1 column on mobile
- Test with theme preview on mobile device

---

## 🎯 Next Steps

1. ✅ Install the section (follow steps above)
2. 🎨 Customize colors to match your brand
3. ✏️ Edit or add your own reviews
4. 📱 Test on mobile and desktop
5. 🚀 Publish your changes

---

## 💡 Pro Tips

- **Position**: Place after partner banner for maximum trust impact
- **CTA**: Add a button below reviews linking to product pages
- **Updates**: Refresh reviews monthly with new testimonials
- **Photos**: Consider replacing avatar initials with actual profile photos
- **Links**: Make reviewer names clickable to Instagram profiles

---

**Need help?** The section is fully documented with comments in the code.
