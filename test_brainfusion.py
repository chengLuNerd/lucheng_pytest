from seleniumbase import BaseCase
import pytest


class TestReview3DSmoke(BaseCase):

    def test_open(self):
        
        URL = "http://localhost:9988/zh-cn/BrainMR/Viewer/Index?StudyUid=1.3.12.2.1107.5.2.36.40495.30000011050900064109300000079&UserId=uih&UserRefid=&sessionId=3i15iyp203byug4pcr4iygp5&RealModality=MR&FilmingSessionId=3i15iyp203byug4pcr4iygp5&FilmingUserRefid=&AppType=8&RenderSeriesId=&FristSeriesModality=MR&NeedPreload=False&OpenType=upr&DataSource=PACS&MsgCode=&DaysToExpired=-1&RisService="
        
        # Navigate to the Review3D page
        self.open(URL)

        # 检查能否显示主框架，排除一些IIS站点异常或者license异常
        self.assert_element('#mainbody')

        # 先等待进度条出现，30s时间内，判断进度条是否消失且进度条要到达100%，
        self.wait_for_element_visible('#progressbar')
        self.wait_for_element_not_visible('#progressbar',timeout=30)
        progressbar_value = self.get_attribute("#progressbar", "aria-valuenow")
        self.assertEqual(progressbar_value, '100')

        # 暂停，检查是否出黑图
        self.click('#horizontal-slider button')

        # 获取canvas图像, 如果需要你可以使用base64解码保存成jpg文件
        # pytest.set_trace()
        canvas = self.find_elements('#canvas_0_0')[0]
        canvas_base64 = self.driver.execute_script("\
            var canvas= arguments[0];\
            var data = canvas.toDataURL('image/png').substring(22);\
            return data;", canvas)
        # 暂时通过base64字符串长度来判断黑图，最优的方式这个base64字符串的比较就可以？或者保存下来是通过图像识别？
        self.assertTrue(len(canvas_base64) > 2040)

