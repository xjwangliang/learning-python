package com.taobao.api.domain;

import java.util.Date;
import java.util.List;

import com.taobao.api.TaobaoObject;
import com.taobao.api.internal.mapping.ApiField;
import com.taobao.api.internal.mapping.ApiListField;

/**
 * 机票业务订单
 *
 * @author auto create
 * @since 1.0, null
 */
public class EtOrder extends TaobaoObject {

	private static final long serialVersionUID = 4823242779823671176L;

	/**
	 * 航空公司名称
	 */
	@ApiField("airline")
	private String airline;

	/**
	 * 往返订单中另一单的订单号
	 */
	@ApiField("another_order_id")
	private Long anotherOrderId;

	/**
	 * 到达城市三字码
	 */
	@ApiField("arr_city")
	private String arrCity;

	/**
	 * 航班到达时间
	 */
	@ApiField("arr_time")
	private Date arrTime;

	/**
	 * 订票状态，init：初始状态，hksuccess：hk成功，hkfailed：hk失败，ticketsuccess：出票成功，ticketfailed：出票失败，xepnrsuccess：取消pnr成功，xepnrfailed：取消pnr失败
	 */
	@ApiField("book_status")
	private String bookStatus;

	/**
	 * 出票方式，
artificial:人工出票, 
autoticket:自动出票,
autobooking:自动hk但不自动出票
	 */
	@ApiField("book_way")
	private String bookWay;

	/**
	 * 舱位代码
	 */
	@ApiField("cabin_code")
	private String cabinCode;

	/**
	 * 总佣金，单位为分
	 */
	@ApiField("commission")
	private Long commission;

	/**
	 * 订单创建时间
	 */
	@ApiField("create_date")
	private Date createDate;

	/**
	 * 出发城市三字码
	 */
	@ApiField("dep_city")
	private String depCity;

	/**
	 * 航班起飞时间
	 */
	@ApiField("dep_time")
	private Date depTime;

	/**
	 * 产品相关功能标志
第一位(2 ^ 0) : 是否需要paidok 1 是 0 否
第二位(2 ^ 1) : paiok成功是否成功 1 是 0 否
第三位(2 ^ 2) : 买家是否修改过订单 1 是 0 否
第四位(2^3):是否是快速购 1是 0否
第五位(2^4)：是否是活动订单，1是 0否
	 */
	@ApiField("flag")
	private Long flag;

	/**
	 * 航班号
	 */
	@ApiField("flight_no")
	private String flightNo;

	/**
	 * 飞机机型
	 */
	@ApiField("flight_type")
	private String flightType;

	/**
	 * 授信金额，单位为分
	 */
	@ApiField("guarantee")
	private Long guarantee;

	/**
	 * 订单备注信息
	 */
	@ApiField("memo")
	private String memo;

	/**
	 * 订单修改时间
	 */
	@ApiField("modify_date")
	private Date modifyDate;

	/**
	 * 订单id
	 */
	@ApiField("order_id")
	private Long orderId;

	/**
	 * 外部产品id
	 */
	@ApiField("out_product_id")
	private String outProductId;

	/**
	 * 乘机人信息列表
	 */
	@ApiListField("passengers")
	@ApiField("passenger")
	private List<Passenger> passengers;

	/**
	 * 淘宝产品id
	 */
	@ApiField("product_id")
	private Long productId;

	/**
	 * 产品（政策）类型。现有：COMMON_SPECIAL_PRICE（特价-普通），RESTRICTED_SPECIAL_PRICE（特价-限售），RETURN_FEE(让利)，SPECIAL(特殊)四种产品
	 */
	@ApiField("product_type")
	private String productType;

	/**
	 * 退改签规则
	 */
	@ApiField("refund_msg")
	private String refundMsg;

	/**
	 * 联系人邮箱
	 */
	@ApiField("relation_email")
	private String relationEmail;

	/**
	 * 联系人姓名
	 */
	@ApiField("relation_name")
	private String relationName;

	/**
	 * 联系人电话，可以是手机，或座机
	 */
	@ApiField("relation_tel")
	private String relationTel;

	/**
	 * 联系人旺旺
	 */
	@ApiField("relation_ww")
	private String relationWw;

	/**
	 * 机票代理商id
	 */
	@ApiField("seller_id")
	private Long sellerId;

	/**
	 * 机票代理商名称
	 */
	@ApiField("seller_name")
	private String sellerName;

	/**
	 * 机票代理商电话，可能是座机，也可能是手机
	 */
	@ApiField("seller_phone")
	private String sellerPhone;

	/**
	 * 机票代理商旺旺
	 */
	@ApiField("seller_ww")
	private String sellerWw;

	/**
	 * 1: 未提交（买家未支付订金）
2: 失效（未支付订金超时）
3: 未处理（废弃）
4: 处理中（买家已支付订金，卖家还未受理）
5: 成功（订票成功）
8: 成功（扣佣金成功）
9: 成功（扣佣金失败）
10: 失败（订票失败）
11: 失败（解冻成功）
12: 失败（解冻失败）
13: 取消（买家在未付款（或已经付款而支付宝没有通知淘宝）时取消）
14: 取消（买家取消订单）
15: 取消（解冻成功）
16: 取消（解冻失败）
17: 失效（卖家未受理超时）
18: 失效（解冻成功）
19: 失效（解冻失败）
20: 失效（卖家处理中超时）
21: 失效（解冻成功）
22: 失效（解冻失败）
23: 集团订单成功
24: 集团订单失败
25: 行政购票扣款成功
26: 行政购票扣款失败
27: 在hk阶段失败(一般由自动hk失败引起)
28、确定出票
	 */
	@ApiField("status")
	private Long status;

	/**
	 * 经停：stop ，
直飞：nostop
	 */
	@ApiField("stop")
	private String stop;

	/**
	 * 票价，以分为单位
	 */
	@ApiField("total_price")
	private Long totalPrice;

	/**
	 * 配送地址 省-市-区-地址
	 */
	@ApiField("traffic_addr")
	private String trafficAddr;

	/**
	 * 接收人电话
	 */
	@ApiField("traffic_phone")
	private String trafficPhone;

	/**
	 * 配送地址邮编
	 */
	@ApiField("traffic_post")
	private String trafficPost;

	/**
	 * 接收人
	 */
	@ApiField("traffic_receiver")
	private String trafficReceiver;

	/**
	 * 航程类型 departure：去程 back：回程
	 */
	@ApiField("trip_seg")
	private String tripSeg;

	/**
	 * 订单类型 single:单程 round：往返
	 */
	@ApiField("trip_type")
	private String tripType;

	public String getAirline() {
		return this.airline;
	}
	public void setAirline(String airline) {
		this.airline = airline;
	}

	public Long getAnotherOrderId() {
		return this.anotherOrderId;
	}
	public void setAnotherOrderId(Long anotherOrderId) {
		this.anotherOrderId = anotherOrderId;
	}

	public String getArrCity() {
		return this.arrCity;
	}
	public void setArrCity(String arrCity) {
		this.arrCity = arrCity;
	}

	public Date getArrTime() {
		return this.arrTime;
	}
	public void setArrTime(Date arrTime) {
		this.arrTime = arrTime;
	}

	public String getBookStatus() {
		return this.bookStatus;
	}
	public void setBookStatus(String bookStatus) {
		this.bookStatus = bookStatus;
	}

	public String getBookWay() {
		return this.bookWay;
	}
	public void setBookWay(String bookWay) {
		this.bookWay = bookWay;
	}

	public String getCabinCode() {
		return this.cabinCode;
	}
	public void setCabinCode(String cabinCode) {
		this.cabinCode = cabinCode;
	}

	public Long getCommission() {
		return this.commission;
	}
	public void setCommission(Long commission) {
		this.commission = commission;
	}

	public Date getCreateDate() {
		return this.createDate;
	}
	public void setCreateDate(Date createDate) {
		this.createDate = createDate;
	}

	public String getDepCity() {
		return this.depCity;
	}
	public void setDepCity(String depCity) {
		this.depCity = depCity;
	}

	public Date getDepTime() {
		return this.depTime;
	}
	public void setDepTime(Date depTime) {
		this.depTime = depTime;
	}

	public Long getFlag() {
		return this.flag;
	}
	public void setFlag(Long flag) {
		this.flag = flag;
	}

	public String getFlightNo() {
		return this.flightNo;
	}
	public void setFlightNo(String flightNo) {
		this.flightNo = flightNo;
	}

	public String getFlightType() {
		return this.flightType;
	}
	public void setFlightType(String flightType) {
		this.flightType = flightType;
	}

	public Long getGuarantee() {
		return this.guarantee;
	}
	public void setGuarantee(Long guarantee) {
		this.guarantee = guarantee;
	}

	public String getMemo() {
		return this.memo;
	}
	public void setMemo(String memo) {
		this.memo = memo;
	}

	public Date getModifyDate() {
		return this.modifyDate;
	}
	public void setModifyDate(Date modifyDate) {
		this.modifyDate = modifyDate;
	}

	public Long getOrderId() {
		return this.orderId;
	}
	public void setOrderId(Long orderId) {
		this.orderId = orderId;
	}

	public String getOutProductId() {
		return this.outProductId;
	}
	public void setOutProductId(String outProductId) {
		this.outProductId = outProductId;
	}

	public List<Passenger> getPassengers() {
		return this.passengers;
	}
	public void setPassengers(List<Passenger> passengers) {
		this.passengers = passengers;
	}

	public Long getProductId() {
		return this.productId;
	}
	public void setProductId(Long productId) {
		this.productId = productId;
	}

	public String getProductType() {
		return this.productType;
	}
	public void setProductType(String productType) {
		this.productType = productType;
	}

	public String getRefundMsg() {
		return this.refundMsg;
	}
	public void setRefundMsg(String refundMsg) {
		this.refundMsg = refundMsg;
	}

	public String getRelationEmail() {
		return this.relationEmail;
	}
	public void setRelationEmail(String relationEmail) {
		this.relationEmail = relationEmail;
	}

	public String getRelationName() {
		return this.relationName;
	}
	public void setRelationName(String relationName) {
		this.relationName = relationName;
	}

	public String getRelationTel() {
		return this.relationTel;
	}
	public void setRelationTel(String relationTel) {
		this.relationTel = relationTel;
	}

	public String getRelationWw() {
		return this.relationWw;
	}
	public void setRelationWw(String relationWw) {
		this.relationWw = relationWw;
	}

	public Long getSellerId() {
		return this.sellerId;
	}
	public void setSellerId(Long sellerId) {
		this.sellerId = sellerId;
	}

	public String getSellerName() {
		return this.sellerName;
	}
	public void setSellerName(String sellerName) {
		this.sellerName = sellerName;
	}

	public String getSellerPhone() {
		return this.sellerPhone;
	}
	public void setSellerPhone(String sellerPhone) {
		this.sellerPhone = sellerPhone;
	}

	public String getSellerWw() {
		return this.sellerWw;
	}
	public void setSellerWw(String sellerWw) {
		this.sellerWw = sellerWw;
	}

	public Long getStatus() {
		return this.status;
	}
	public void setStatus(Long status) {
		this.status = status;
	}

	public String getStop() {
		return this.stop;
	}
	public void setStop(String stop) {
		this.stop = stop;
	}

	public Long getTotalPrice() {
		return this.totalPrice;
	}
	public void setTotalPrice(Long totalPrice) {
		this.totalPrice = totalPrice;
	}

	public String getTrafficAddr() {
		return this.trafficAddr;
	}
	public void setTrafficAddr(String trafficAddr) {
		this.trafficAddr = trafficAddr;
	}

	public String getTrafficPhone() {
		return this.trafficPhone;
	}
	public void setTrafficPhone(String trafficPhone) {
		this.trafficPhone = trafficPhone;
	}

	public String getTrafficPost() {
		return this.trafficPost;
	}
	public void setTrafficPost(String trafficPost) {
		this.trafficPost = trafficPost;
	}

	public String getTrafficReceiver() {
		return this.trafficReceiver;
	}
	public void setTrafficReceiver(String trafficReceiver) {
		this.trafficReceiver = trafficReceiver;
	}

	public String getTripSeg() {
		return this.tripSeg;
	}
	public void setTripSeg(String tripSeg) {
		this.tripSeg = tripSeg;
	}

	public String getTripType() {
		return this.tripType;
	}
	public void setTripType(String tripType) {
		this.tripType = tripType;
	}

}
